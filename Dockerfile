FROM alpine:3.7
EXPOSE 7000
RUN apk add --update python2 py-pip 
COPY src /
RUN pip install -r requirements.txt
RUN chmod +x /run.sh
CMD ["sh", "/run.sh"]


