#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
import datetime

#用户表
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)  #id
    username = db.Column(db.String(30))    #用户名
    userpassword = db.Column(db.String(30))    #密码
    user_remarks = db.Column(db.String(30))    #预留字段


#角色表
class UserRole(db.Model):
    __tablename__ = 'userrole'
    role_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)  #id
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))  # 用户id
    role_name = db.Column(db.String(30))   #角色名
    role_remarks = db.Column(db.String(50))    #角色说明


#项目管理表
class ProjectManage(db.Model):
    __tablename__ = 'projectmanage'
    project_id = db.Column(db.Integer,unique=True, primary_key=True, autoincrement=True)    #id
    project_name = db.Column(db.String(30))     #项目名称
    project_type = db.Column(db.String(20))     #项目类型
    role_id = db.Column(db.Integer, db.ForeignKey("userrole.role_id"))  # 角色id
    case_num = db.Column(db.Integer)            #用例数
    project_status = db.Column(db.String(20))   #项目状态
    project_createtime = db.Column(db.DateTime)             #项目创建时间
    project_endtime = db.Column(db.DateTime)                #项目结束时间
    project_remarks = db.Column(db.String(200))    #备注


#接口列表
class Interface(db.Model):
    __tablename__ = 'interface'
    id = db.Column(db.Integer,unique=True, primary_key=True, autoincrement=True)    #id
    project_id = (db.Integer, db.ForeignKey("projectmanage.project_id"))    #项目id
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))  # 用户id
    name = db.Column(db.String(30))     #接口名称
    url = db.Column(db.String(50))      #接口地址
    method = db.Column(db.String(20))   #请求方式
    casenum = db.Column(db.Integer)        #用例数
    tasknum = db.Column(db.Integer)     #任务数
    status = db.Column(db.String(20))   #接口状态
    cover = db.Column(db.String(10))    #是否覆盖
    createtime =db.Column(db.DateTime)      #创建时间
    remarks = db.Column(db.String())    #备注

#参数表
class Parameter(db.Model):
        __tablename__ = 'parameter'
        id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)  # id
        interface_id = (db.Integer, db.ForeignKey("interface.id"))  # 接口id
        name = db.Column(db.String(50))     #参数名称
        value = db.Column(db.String(200))     #参数值
        type = db.Column(db.String(30))     #参数类型
#用例表
class UserCase(db.Model):
    __tablename__ = 'usercase'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)  # id
    interface_id = (db.Integer, db.ForeignKey("interface.id"))  # 接口id
    project_id = (db.Integer, db.ForeignKey("projectmanage.project_id"))  # 项目id
    name = db.Column(db.String(30))     #用例名
    content = db.Column(db.String(100))             #用例内容
    createuserid =db.Column(db.Integer, db.ForeignKey("user.user_id"))  # 用户id
    createtime = db.Column(db.DateTime)             #创建时间
    remarks = db.Column(db.String())    #备注

#报告表
class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)  # id
    usercase_id = (db.Integer, db.ForeignKey("usercase.id"))        #用例id
    route = db.Column(db.String(30))        #路劲
    time = db.Column(db.DateTime)       #时间
