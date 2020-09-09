FROM python:3.6
WORKDIR /
ADD https://raw.githubusercontent.com/karthikbanoor/flask-crud-app/master/git_clone_and_run.sh /
RUN chmod +x /git_clone_and_run.sh
ENTRYPOINT ["/git_clone_and_run.sh"]
