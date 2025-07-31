# WadeRepoNJR201
WadeRepoNJR201

# 用 pyenv 安裝 Python 3.8.10 版本 (它會把 Python 安裝到 ~/.pyenv/versions/ 目錄下)
pyenv install 3.8.10

# 設定全域（global）預設的 Python 版本為 3.8.10 (執行後 python 就會指向 ~/.pyenv/versions/3.8.10/bin/python)
pyenv global 3.8.10

# 設定目前資料夾的 Python 版本為 3.8.10 (pyenv 會在當前資料夾（這裡是 ~/WadeRepoNJR201/）寫入一個 .python-version 檔案，內容就是 3.8.10，)
# 從此以後，在這個資料夾或其子資料夾中執行 python 就會使用 3.8.10
# local > global 的優先權，所以這會覆蓋 pyenv global 的設定
pyenv local 3.8.10

# 在目前的 Python（也就是 pyenv 的 3.8.10）環境下安裝特定版本的 pipenv 工具
# pipenv 是一個用來管理虛擬環境和套件（依照 Pipfile）的工具
pip install pipenv==2022.4.8

# 用指定的 Python 執行檔建立 pipenv 虛擬環境
# 叫 pipenv 使用 ~/.pyenv/versions/3.8.10/bin/python 這個 特定版本的 Python 在你當前的資料夾（例如 ~/WadeRepoNJR201/）中 建立一個新的虛擬環境
# 建立後會產生.venv/ 資料夾（或是放在其他地方，依照 pipenv 設定）、Pipfile 檔案、Pipfile.lock
pipenv --python ~/.pyenv/versions/3.8.10/bin/python

# 更新Pilfile.lock (依 Pipfile 安裝相容的最新版套件)
pipenv install

# 安裝Package
pipenv install flask==2.3.3

# 單純在當下環境使用Python
python

# 在虛擬的Python環境下使用Python
pipenv run python

# 建立package
pipenv install -e .

# 同步別人repo環境，依照 Pipfile.lock 同步安裝環境
pipenv sync

# 選擇 VS Code 要使用的 Python 虛擬環境
Ctrl+Shift+P → Python: Select Interpreter

#  查看所有 container（含已停止的）
docker ps -a

# 查看所有 image
docker images

#  停止單一 container
docker stop <container_id_or_name>


# 停止所有 container
docker stop $(docker ps -aq)

# 刪除單一 container
docker rm <container_id_or_name>

# 刪除所有已停止的 container
docker container prune -f

# 強制刪除所有 container
docker rm -f $(docker ps -aq)

# 刪除單一 image
docker rmi <image_id_or_name>

# 刪除所有 image
docker rmi -f $(docker images -aq)


# 啟動yml
docker compose -f {某名稱}.yml up -d 

# 關閉yml
docker compose -f {某名稱}.yml down

# RabbitMQ
http://127.0.0.1:15672/

# Flower
http://127.0.0.1:5555/

# 查看Docker Container(還活著的 container)
docker ps

# 查看Docker Container(所有的 container)
docker ps -a

# 查看 container log
docker logs {Container名稱}

# 安裝celery (它是python package)
pipenv install celery==5.5.0

# 安裝package
pipenv install {package名稱}

# producer 發送任務
pipenv run python {package名稱}/producer.py

# 啟動工人
pipenv run celery -A {package名稱}.worker worker --loglevel=info -E

# 啟動工人接收特定任務
pipenv run celery -A {package名稱}.worker worker -Q {任務1},{任務2} --loglevel=info -E

# 啟動多個工人(一個Terminal一個工人)=>這就是分散式
pipenv run celery -A {package名稱}.worker worker -n worker1 --loglevel=info -E
pipenv run celery -A {package名稱}.worker worker -n worker2 --loglevel=info -E

# 指定某工人接某任務
pipenv run celery -A {package名稱}.worker worker -Q {任務1} -n worker1 --loglevel=info -E
pipenv run celery -A {package名稱}.worker worker -Q {任務2} -n worker2 --loglevel=info -E

# 建立image
# -f: 指定 Dockerfile 名稱、路徑
# -t: 建立 image 的名稱
docker build -f Dockerfile -t {docker帳號}/{image名稱}:0.0.1 .

# 刪除image
docker rmi {docker帳號}/{image名稱}:0.0.1

# 上傳image至GitHub
docker push {docker帳號}/{image名稱}:0.0.1

# 啟動 docker-compose
docker compose -f {yml名稱}.yml up -d

# 建立network
docker network create {network名稱}

# 查看network
docker network ls

# 查看network 被誰使用
docker network inspect {network名稱}

# MySQL
http://127.0.0.1:8000/

# 查看 volume
docker volume ls

# 上傳資料到mysql
pipenv run python crawlerWade/upload_data_to_mysql.py

# 建立環境變數.env
ENV=DEV python genenv.py
ENV=DOCKER python genenv.py
ENV=PRODUCTION python genenv.py

# 啟動yml (依照指定的image)
DOCKER_IMAGE_VERSION={image 版本} docker compose -f {yml名稱}.yml up -d
# 關閉yml (依照指定的image)
DOCKER_IMAGE_VERSION={image 版本} docker compose -f {yml名稱}.yml down
