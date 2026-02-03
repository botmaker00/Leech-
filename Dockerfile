FROM mysterysd/wzmlx:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# copy files
COPY . .

# force clean reinstall of pyrogram
RUN pip3 uninstall -y pyrogram tgcrypto && \
    pip3 install --no-cache-dir -U pyrogram tgcrypto && \
    pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
