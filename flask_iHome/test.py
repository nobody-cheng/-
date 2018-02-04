@api.route("/users/name", methods=["PUT"])
@login_required
def reset_name():
    """修改用户名"""
    # user_id = g.user_id
    user_id = session.get("user_id")
    req_dict = request.get_json()
    name = req_dict.get("name")
    print name
    try:
        user = User.query.filter_by(id=user_id).first()
        user_name = User.query.filter_by(name=name).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据库失败")
    if user is not None:
        if user_name is not None:
            return jsonify(errno=RET.DATAEXIST, errmsg="用户名已存在，无法修改")
        user.name = name
        print name
        try:
            db.session.commit()
        except IntegrityError as e:
            # 数据库操作错误后的回滚
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="修改数据库异常")
    else:
        return jsonify(errno=RET.USERERR, errmsg="用户不存在或未激活")
    # 修改session
    session["name"] = name

    return jsonify(errno=RET.OK, errmsg="成功")