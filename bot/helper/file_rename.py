import re
import os
import unicodedata
from bot import user_data, config_dict, LOGGER

# Constants
MAX_COLLISION_ATTEMPTS = 1000  # Maximum attempts to find a unique filename
COLLISION_PADDING = 5  # Extra characters reserved for collision numbering like " (1)"

def extract_episode_number(filename):
    if not filename:
        return None
    quality_and_year_indicators = [
        r'\d{2,4}[pP]', r'\dK', r'HD(?:RIP)?', r'WEB(?:-)?DL', r'BLURAY',
        r'X264', r'X265', r'HEVC', r'FHD', r'UHD', r'HDR', r'H\.264', r'H\.265',
        r'(?:19|20)\d{2}', r'Multi(?:audio)?', r'Dual(?:audio)?',
    ]
    quality_pattern_for_exclusion = r'(?:' + '|'.join([f'(?:[\s._-]*{ind})' for ind in quality_and_year_indicators]) + r')'
    patterns = [
        re.compile(r'S\d+[.-_]?E(\d+)', re.IGNORECASE),
        re.compile(r'(?:Episode|EP)[\s._-]*(\d+)', re.IGNORECASE),
        re.compile(r'\bE(\d+)\b', re.IGNORECASE),
        re.compile(r'[\[\(]E(\d+)[\]\)]', re.IGNORECASE),
        re.compile(r'\b(\d+)\s*of\s*\d+\b', re.IGNORECASE),
        re.compile(
            r'(?:^|[^0-9A-Z])'
            r'(\d{1,4})'
            r'(?:[^0-9A-Z]|$)'
            r'(?!' + quality_pattern_for_exclusion + r')'
            , re.IGNORECASE
        ),
    ]
    for i, pattern in enumerate(patterns):
        matches = pattern.findall(filename)
        if matches:
            for match in matches:
                try:
                    if isinstance(match, tuple):
                        episode_str = match[0]
                    else:
                        episode_str = match
                    episode_num = int(episode_str)
                    if 1 <= episode_num <= 9999:
                        if episode_num in [360, 480, 720, 1080, 1440, 2160, 2020, 2021, 2022, 2023, 2024, 2025]:
                            if re.search(r'\b' + str(episode_num) + r'(?:p|K|HD|WEB|BLURAY|X264|X265|HEVC|Multi|Dual)\b', filename, re.IGNORECASE) or \
                                re.search(r'\b(?:19|20)\d{2}\b', filename, re.IGNORECASE) and len(str(episode_num)) == 4:
                                continue
                        return episode_num
                except ValueError:
                    continue
    return None

def extract_season_number(filename):
    if not filename:
        return None
    quality_and_year_indicators = [
        r'\d{2,4}[pP]', r'\dK', r'HD(?:RIP)?', r'WEB(?:-)?DL', r'BLURAY',
        r'X264', r'X265', r'HEVC', r'FHD', r'UHD', r'HDR', r'H\.264', r'H\.265',
        r'(?:19|20)\d{2}', r'Multi(?:audio)?', r'Dual(?:audio)?',
    ]
    quality_pattern_for_exclusion = r'(?:' + '|'.join([f'(?:[\s._-]*{ind})' for ind in quality_and_year_indicators]) + r')'
    patterns = [
        re.compile(r'S(\d+)[._-]?E\d+', re.IGNORECASE),
        re.compile(r'(?:Season|SEASON|season)[\s._-]*(\d+)', re.IGNORECASE),
        re.compile(r'\bS(\d+)\b(?!E\d)', re.IGNORECASE),
        re.compile(r'[\[\(]S(\d+)[\]\)]', re.IGNORECASE),
        re.compile(r'[._-]S(\d+)(?:[._-]|$)', re.IGNORECASE),
    ]
    for i, pattern in enumerate(patterns):
        match = pattern.search(filename)
        if match:
            try:
                season_num = int(match.group(1))
                if 1 <= season_num <= 99:
                    return season_num
            except ValueError:
                continue
    return None

def extract_audio_info(filename):
    """Extract audio information from filename, including languages and 'dual'/'multi'."""
    audio_keywords = {
        'Hindi': re.compile(r'Hindi', re.IGNORECASE), 'English': re.compile(r'English', re.IGNORECASE),
        'Multi': re.compile(r'Multi(?:audio)?', re.IGNORECASE), 'Telugu': re.compile(r'Telugu', re.IGNORECASE),
        'Eng': re.compile(r'Eng', re.IGNORECASE), 'Sub': re.compile(r'Sub', re.IGNORECASE),
        'Eng sub': re.compile(r'Eng sub', re.IGNORECASE), 'Dub': re.compile(r'Dub', re.IGNORECASE),
        'Eng dub': re.compile(r'Eng dub', re.IGNORECASE), 'Tamil': re.compile(r'Tamil', re.IGNORECASE),
        'Jap': re.compile(r'Jap', re.IGNORECASE), 'Dual': re.compile(r'Dual(?:audio)?', re.IGNORECASE),
        'AAC': re.compile(r'AAC', re.IGNORECASE), 'AC3': re.compile(r'AC3', re.IGNORECASE),
        'DTS': re.compile(r'DTS', re.IGNORECASE), 'MP3': re.compile(r'MP3', re.IGNORECASE),
        '5.1': re.compile(r'5\.1', re.IGNORECASE), '2.0': re.compile(r'2\.0', re.IGNORECASE),
    }
    detected_audio = []
    if re.search(r'\bMulti(?:audio)?\b', filename, re.IGNORECASE):
        detected_audio.append("Multi")
    if re.search(r'\bDual(?:audio)?\b', filename, re.IGNORECASE):
        detected_audio.append("Dual")
    priority_keywords = ['Hindi', 'English', 'Telugu', 'Tamil', 'Eng', 'Sub', 'Eng sub', 'Dub', 'Eng dub', 'Jap']
    for keyword in priority_keywords:
        if audio_keywords[keyword].search(filename) and keyword not in detected_audio:
            detected_audio.append(keyword)
    for keyword in ['AAC', 'AC3', 'DTS', 'MP3', '5.1', '2.0']:
        if audio_keywords[keyword].search(filename) and keyword not in detected_audio:
            detected_audio.append(keyword)
    detected_audio = list(dict.fromkeys(detected_audio))
    return ' '.join(detected_audio) if detected_audio else None

def extract_quality(filename):
    """Extract video quality from filename."""
    patterns = [
        re.compile(r'\b(4K|2K|2160p|1440p|1080p|720p|480p|360p)\b', re.IGNORECASE),
        re.compile(r'\b(HD(?:RIP)?|WEB(?:-)?DL|BLURAY)\b', re.IGNORECASE),
        re.compile(r'\b(X264|X265|HEVC)\b', re.IGNORECASE),
    ]
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            found_quality = match.group(1)
            if found_quality.lower() in ["4k", "2k", "hdrip", "web-dl", "bluray"]:
                return found_quality.upper() if found_quality.upper() in ["4K", "2K"] else found_quality.capitalize()
            return found_quality
    return None

def get_new_name(original_name, user_id):
    user_dict = user_data.get(user_id, {})
    format_template = user_dict.get('format')
    if not format_template:
        return original_name

    episode_number = extract_episode_number(original_name)
    season_number = extract_season_number(original_name)
    audio_info_extracted = extract_audio_info(original_name)
    quality_extracted = extract_quality(original_name)

    season_value_formatted = str(season_number).zfill(2) if season_number is not None else "01"
    episode_value_formatted = str(episode_number).zfill(2) if episode_number is not None else "01"

    template = format_template.format(
        season=season_value_formatted,
        episode=episode_value_formatted,
        quality=quality_extracted or "",
        audio=audio_info_extracted or ""
    )

    template = re.sub(r'\[\s*\]', '', template)
    template = re.sub(r'\(\s*\)', '', template)
    template = re.sub(r'\{\s*\}', '', template)

    _, file_extension = os.path.splitext(original_name)
    return f"{template}{file_extension}"


def is_archive_part(filename):
    """Detect multi-part archive files that should not be renamed before extraction."""
    archive_part_patterns = [
        r'\.part\d+\.rar$',  # .part1.rar, .part01.rar
        r'\.r\d{2,}$',       # .r00, .r01, .r99 (at least 2 digits)
        r'\.z\d{2,}$',       # .z01, .z02 (at least 2 digits)
        r'\.\d{3}$',         # .001, .002, .003 (exactly 3 digits)
        r'\.7z\.\d+$',       # .7z.001
        r'\.zip\.\d+$',      # .zip.001
    ]
    for pattern in archive_part_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            return True
    return False


def sanitize_filename(name, sanitize=True, spaces_mode='space', case_mode='keep', max_len=128):
    """Sanitize filename by removing illegal characters and applying transformations."""
    if not sanitize:
        return name
    
    # Normalize Unicode (use NFC to preserve character appearance while normalizing)
    name = unicodedata.normalize('NFC', name)
    
    # Remove or replace illegal filesystem characters
    illegal_chars = r'[<>:"/\\|?*\x00-\x1f]'
    name = re.sub(illegal_chars, '', name)
    
    # Handle spaces
    if spaces_mode == 'underscore':
        name = name.replace(' ', '_')
    elif spaces_mode == 'dot':
        name = name.replace(' ', '.')
    
    # Apply case transformation
    if case_mode == 'lower':
        name = name.lower()
    elif case_mode == 'upper':
        name = name.upper()
    
    # Apply max length (preserve extension)
    if len(name) > max_len:
        base, ext = os.path.splitext(name)
        # Always preserve the extension, truncate base if needed
        if ext:
            # Leave space for collision numbering like " (1)"
            available_len = max(max_len - len(ext) - COLLISION_PADDING, 10)
            base = base[:available_len]
            name = base + ext
        else:
            # No extension, just truncate
            name = name[:max_len]
    
    return name


def build_renamed_path(original_name, user_id, prefix='', suffix='', sanitize=True, 
                       spaces_mode='space', case_mode='keep', max_len=128):
    """Build new name using existing rename logic plus additional transformations."""
    # Get base name and extension
    base_name, ext = os.path.splitext(original_name)
    
    # Apply user-specific format if available (only if user_id is provided)
    if user_id is not None:
        # Check if user has a format template first
        user_dict = user_data.get(user_id, {})
        has_format = bool(user_dict.get('format'))
        
        if has_format:
            # Apply the format
            new_name = get_new_name(original_name, user_id)
            # Apply prefix/suffix to the formatted name if specified
            if prefix or suffix:
                new_base, new_ext = os.path.splitext(new_name)
                new_name = f"{prefix}{new_base}{suffix}{new_ext}"
        elif prefix or suffix:
            # No format, just apply prefix/suffix
            new_name = f"{prefix}{base_name}{suffix}{ext}"
        else:
            # No format and no prefix/suffix, keep original
            new_name = original_name
    else:
        # No user_id, just apply prefix/suffix
        if prefix or suffix:
            new_name = f"{prefix}{base_name}{suffix}{ext}"
        else:
            new_name = original_name
    
    # Sanitize the final name
    new_name = sanitize_filename(new_name, sanitize, spaces_mode, case_mode, max_len)
    
    return new_name


def apply_auto_rename(base_dir, user_id, skip_archive_parts=True):
    """
    Apply auto-rename using config_dict settings.
    Helper function to avoid code duplication.
    
    Args:
        base_dir: Directory to rename
        user_id: User ID for format-based renaming
        skip_archive_parts: Whether to skip archive parts
    
    Returns:
        Tuple of (renamed_base_dir, list of changes)
    """
    if not config_dict.get('AUTO_RENAME'):
        return base_dir, []
    
    return rename_tree(
        base_dir,
        user_id=user_id,
        multi_mode=config_dict.get('RENAME_MULTI', 'per-file'),
        sanitize=config_dict.get('RENAME_SANITIZE', True),
        spaces_mode=config_dict.get('RENAME_SPACES', 'space'),
        case_mode=config_dict.get('RENAME_CASE', 'keep'),
        max_len=config_dict.get('RENAME_MAX_LEN', 128),
        prefix=config_dict.get('RENAME_PREFIX', ''),
        suffix=config_dict.get('RENAME_SUFFIX', ''),
        skip_archive_parts=skip_archive_parts
    )


def rename_tree(base_dir, user_id=None, multi_mode='per-file', sanitize=True, 
                spaces_mode='space', case_mode='keep', max_len=128, 
                prefix='', suffix='', skip_archive_parts=True):
    """
    Recursively rename files and folders in a directory tree.
    
    Args:
        base_dir: Root directory to process
        user_id: User ID for format-based renaming (optional)
        multi_mode: 'per-file', 'root-folder-only', or 'both'
        sanitize: Apply filename sanitization
        spaces_mode: 'space', 'underscore', or 'dot'
        case_mode: 'keep', 'lower', or 'upper'
        max_len: Maximum filename length
        prefix: Prefix to add to filenames
        suffix: Suffix to add to filenames
        skip_archive_parts: Skip renaming multi-part archives before extraction
    
    Returns:
        Tuple of (renamed_base_dir, list of (old_path, new_path) changes)
    """
    if not os.path.exists(base_dir):
        LOGGER.warning(f'rename_tree: Path does not exist: {base_dir}')
        return base_dir, []
    
    changes = []
    
    # Process files and folders bottom-up to avoid path invalidation
    # With topdown=False, subdirectories are processed before their parents,
    # so renaming a directory won't affect the traversal
    for root, dirs, files in os.walk(base_dir, topdown=False):
        # Rename files first (if per-file mode)
        if multi_mode in ['per-file', 'both']:
            for filename in files:
                # Skip archive parts if requested
                if skip_archive_parts and is_archive_part(filename):
                    LOGGER.info(f'Skipping archive part: {filename}')
                    continue
                
                old_path = os.path.join(root, filename)
                
                # Build new name
                if user_id is not None:
                    new_name = build_renamed_path(filename, user_id, prefix, suffix, 
                                                   sanitize, spaces_mode, case_mode, max_len)
                else:
                    new_name = sanitize_filename(f"{prefix}{filename}{suffix}", sanitize, 
                                                 spaces_mode, case_mode, max_len)
                
                # Handle collisions
                if new_name != filename:
                    new_path = os.path.join(root, new_name)
                    counter = 1
                    base, ext = os.path.splitext(new_name)
                    while os.path.exists(new_path) and counter < MAX_COLLISION_ATTEMPTS:
                        new_name = f"{base} ({counter}){ext}"
                        new_path = os.path.join(root, new_name)
                        counter += 1
                    
                    if counter >= MAX_COLLISION_ATTEMPTS:
                        LOGGER.error(f'Could not find unique name for {filename} after {MAX_COLLISION_ATTEMPTS} attempts')
                        continue
                    
                    try:
                        os.rename(old_path, new_path)
                        changes.append((old_path, new_path))
                        LOGGER.info(f'Renamed file: {filename} -> {new_name}')
                    except Exception as e:
                        LOGGER.error(f'Failed to rename {old_path}: {e}')
        
        # Rename directories (if per-file or both mode, skip root for root-folder-only)
        if multi_mode in ['per-file', 'both']:
            for dirname in dirs:
                old_path = os.path.join(root, dirname)
                
                # Build new name (folders don't have extensions)
                if user_id is not None:
                    # For folders, treat as file without extension
                    new_name = build_renamed_path(dirname, user_id, prefix, suffix, 
                                                   sanitize, spaces_mode, case_mode, max_len)
                else:
                    new_name = sanitize_filename(f"{prefix}{dirname}{suffix}", sanitize, 
                                                 spaces_mode, case_mode, max_len)
                
                # Handle collisions
                if new_name != dirname:
                    new_path = os.path.join(root, new_name)
                    base_new_name = new_name
                    counter = 1
                    while os.path.exists(new_path) and counter < MAX_COLLISION_ATTEMPTS:
                        new_name = f"{base_new_name} ({counter})"
                        new_path = os.path.join(root, new_name)
                        counter += 1
                    
                    if counter >= MAX_COLLISION_ATTEMPTS:
                        LOGGER.error(f'Could not find unique name for directory {dirname} after {MAX_COLLISION_ATTEMPTS} attempts')
                        continue
                    
                    try:
                        os.rename(old_path, new_path)
                        changes.append((old_path, new_path))
                        LOGGER.info(f'Renamed directory: {dirname} -> {new_name}')
                    except Exception as e:
                        LOGGER.error(f'Failed to rename {old_path}: {e}')
    
    # Rename root folder if needed (for root-folder-only or both mode)
    if multi_mode in ['root-folder-only', 'both']:
        parent_dir = os.path.dirname(base_dir)
        root_name = os.path.basename(base_dir)
        
        if user_id is not None:
            new_root_name = build_renamed_path(root_name, user_id, prefix, suffix, 
                                               sanitize, spaces_mode, case_mode, max_len)
        else:
            new_root_name = sanitize_filename(f"{prefix}{root_name}{suffix}", sanitize, 
                                              spaces_mode, case_mode, max_len)
        
        if new_root_name != root_name:
            new_base_dir = os.path.join(parent_dir, new_root_name)
            base_new_root_name = new_root_name
            counter = 1
            while os.path.exists(new_base_dir) and counter < MAX_COLLISION_ATTEMPTS:
                new_root_name = f"{base_new_root_name} ({counter})"
                new_base_dir = os.path.join(parent_dir, new_root_name)
                counter += 1
            
            if counter >= MAX_COLLISION_ATTEMPTS:
                LOGGER.error(f'Could not find unique name for root directory {root_name} after {MAX_COLLISION_ATTEMPTS} attempts')
            else:
                try:
                    os.rename(base_dir, new_base_dir)
                    changes.append((base_dir, new_base_dir))
                    LOGGER.info(f'Renamed root directory: {root_name} -> {new_root_name}')
                    base_dir = new_base_dir
                except Exception as e:
                    LOGGER.error(f'Failed to rename root {base_dir}: {e}')
    
    return base_dir, changes
