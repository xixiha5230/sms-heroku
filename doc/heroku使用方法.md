#### 1.安装 Heroku cli：

`sudo snap install heroku --classic` 

或 

`curl https://cli-assets.heroku.com/install.sh | sh`

#### 2.创建新Heroku APP (python):

`heroku create <app name> --buildpack heroku/python`

#### 3.获取初始python部署包：

`git clone https://github.com/heroku/python-getting-started.git`  && `cd python-getting-started/`

完成后删除`.git`文件，自己再初始化一个git仓库。

#### 4.更改`Procfile`内的内容：

例如改为：`web: python hello_world.py` 就会执行本目录的`hello_world.py`文件

#### 5.修改requirements.txt，添加需要的包

#### 6.更改远程仓库为Heroku：

`heroku git:remote -a <app name>`

#### 7.`commit` git更改

#### 8.提交到Heroku:

`git push heroku master`

#### 9.查看日志:

`heroku logs --tail`