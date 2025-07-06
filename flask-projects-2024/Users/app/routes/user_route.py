from flask import Blueprint, request, jsonify, render_template, redirect, url_for, abort, flash, session
from ..models.user_model import User
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__)

# 首頁(未登入)
@user_bp.route('/')
def home():
    return render_template('index.html')

# 註冊
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        is_owner = data.get('is_owner') == 'on'

        # 檢查使用者是否已存在
        if User.query.filter_by(email=email).first():
            flash('電子郵件已被註冊', 'danger')
            return redirect(url_for('user.register'))

        # 創建新使用者
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            is_owner=is_owner,
            phone='',  # 初始化為空
            bio='',  # 初始化為空
            address=''  # 初始化為空
        )
        db.session.add(new_user)
        db.session.commit()
        flash('註冊成功', 'success')
        return redirect(url_for('user.login'))

    return render_template('register.html')

# 登入
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # 查找使用者
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            # 登入成功
            session['user_id'] = user.id
            session['is_owner'] = user.is_owner
            flash('登入成功', 'success')
            if user.is_owner:
                return redirect(url_for('user.owner_dashboard'))
            else:
                return redirect(url_for('user.guest_dashboard'))
        else:
            # 登入失敗
            flash('無效的電子郵件或密碼', 'danger')
            return redirect(url_for('user.login'))

    return render_template('login.html')

# 登出
@user_bp.route('/logout')
def logout():
    # 處理登出邏輯
    session.pop('user_id', None)
    session.pop('is_owner', None)
    flash('已登出', 'success')
    return redirect(url_for('user.home'))

# 老闆儀表板
@user_bp.route('/owner_dashboard')
def owner_dashboard():
    # 顯示老闆儀表板
    if 'user_id' in session and session.get('is_owner'):
        return render_template('owner_dashboard.html')
    else:
        flash('您沒有權限訪問此頁面', 'danger')
        return redirect(url_for('user.home'))

# 客人儀表板
@user_bp.route('/guest_dashboard')
def guest_dashboard():
    # 顯示客人儀表板
    if 'user_id' in session and not session.get('is_owner'):
        return render_template('guest_dashboard.html')
    else:
        flash('您沒有權限訪問此頁面', 'danger')
        return redirect(url_for('user.home'))

# 編輯個人資料
@user_bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        data = request.form
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        
        if user:
            user.phone = data.get('phone')  # 編輯電話號碼
            user.bio = data.get('bio')  # 編輯簡介
            user.address = data.get('address')  # 編輯地址
            
            db.session.commit()
            flash('個人資料已更新', 'success')
        else:
            flash('使用者不存在', 'danger')
        
        return redirect(url_for('user.edit_profile'))

    user_id = session.get('user_id')
    user = User.query.get(user_id)
    return render_template('edit_profile.html', user=user)

# 查看個人資料
@user_bp.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('profile.html', user=user)
    else:
        flash('使用者不存在', 'danger')
        return redirect(url_for('user.home'))