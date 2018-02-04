import re
from urllib import request

localDir = '/home/python/Desktop/图片/'


d = """"
<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>颜值_颜值直播_颜值精彩视频直播_斗鱼 - 每个人的直播平台</title>
                <meta name="renderer" content="webkit|ie-comp|ie-stand">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
                <meta name="keywords" content="颜值,颜值直播,颜值直播间,颜值直播地址,颜值直播,颜值精彩视频直播">
                        <meta name="description" content="斗鱼直播拥有海量的颜值直播内容,各类热门颜值精彩直播内容全天候不间断,与颜值主播一起零距离互动,全新颜值直播尽在斗鱼直播。">
                <link href="/favicon.ico" type="image/x-icon" rel="icon">
        <link href="/favicon.ico" type="image/x-icon" rel="shortcut icon">

        <link rel="dns-prefetch" href="//shark.douyucdn.cn">
<link rel="dns-prefetch" href="//apic.douyucdn.cn">
<link rel="dns-prefetch" href="//rpic.douyucdn.cn">
<link rel="dns-prefetch" href="//staticlive.douyucdn.cn">
<link rel="dns-prefetch" href="//webconf.douyucdn.cn">
<link rel="dns-prefetch" href="//res.douyucdn.cn">        <script src="//hm.baidu.com/hm.js?e99aee90ec1b2106afe7ec3b199020a7"></script><script type="text/javascript">
    var $SYS = {"cookie_pre":"acf_","web_url":"https:\/\/shark.douyucdn.cn\/","upload_url":"https:\/\/staticlive.douyucdn.cn\/upload\/","res_url":"https:\/\/staticlive.douyucdn.cn\/common\/","res_ver":"v6.887","resource_url":"https:\/\/res.douyucdn.cn\/resource\/","swf_ver":"v6.697","avatar_url":"https:\/\/apic.douyucdn.cn\/","sign_url":"https:\/\/staticlive.douyucdn.cn\/storage\/","sign_newver":false,"pay_site_host":"https:\/\/cz.douyu.com","storage_cdn":"https:\/\/staticlive.douyucdn.cn\/storage\/webpic_resources\/upload\/","tvk":"ccn","tn":"ctn","fh":"https:\/\/dotcounter.douyucdn.cn\/deliver\/fish","fh2":"https:\/\/dotcounter.douyucdn.cn\/deliver\/fish2","fh_edge":"https:\/\/uact.douyucdn.cn\/uact.do","ucp_front":"https:\/\/ucp.douyucdn.cn\/ucp.do","webconfUrl":"https:\/\/webconf.douyucdn.cn\/","pmChatPopwindUrl":"https:\/\/msgstatic.douyu.com","yubaDomain":"\/\/yuba.douyu.com\/","vsite_url":"https:\/\/v.douyu.com"};
    var $DYS = {};
    $DYS['page_init_time'] = new Date().getTime();
        window.passport_host = '//passport.douyu.com/';
    window.client_id = '1';
</script>

<script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/perform/dist/dyl.js?170724"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/shark/lib/js/port/shark-all.js?160113"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/shark/lib/js/lib/jquery.js?160113"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/app/douyu/third/jquery.mCustomScrollbar/jquery.mCustomScrollbar.concat.min.js?170508"></script>
<script>
var _hmt = _hmt || [];
(function() {
	setTimeout(function(){
		var hm = document.createElement("script");
		hm.src = "//hm.baidu.com/hm.js?e99aee90ec1b2106afe7ec3b199020a7";
		var s = document.getElementsByTagName("script")[0];
		s.parentNode.insertBefore(hm, s);
	},0);
})();
</script>
        <script type="text/javascript">
            var $PAGE = {};
            $PAGE.isCate2 = "1";
            $PAGE.cateid = "201";
            $PAGE.pager = {
                count: "3",
                current: "1"
            };
            $PAGE.emperorIcon = "https://res.douyucdn.cn/resource/2017/02/28/common/e3dac153a29afc779a60048ee2fb2d14.gif";
            $PAGE.cate2_id = "201";
            $PAGE.cate1_id = "8";
            var isYzCate = 1;
        </script>

        <link rel="stylesheet" type="text/css" href="https://shark.douyucdn.cn/app/douyu/css/common.css?nv=v6.887"><link rel="stylesheet" type="text/css" href="https://shark.douyucdn.cn/app/douyu/css/com/app-all.css?nv=v6.887"><link rel="stylesheet" type="text/css" href="https://shark.douyucdn.cn/app/douyu/css/page/lives/app-all.css?nv=v6.887">    </head>

    <body data-page-point="2"><div style="display: none; position: absolute;" class=""><div class="aui_outer"><table class="aui_border"><tbody><tr><td class="aui_nw"></td><td class="aui_n"></td><td class="aui_ne"></td></tr><tr><td class="aui_w"></td><td class="aui_c"><div class="aui_inner"><table class="aui_dialog"><tbody><tr><td colspan="2" class="aui_header"><div class="aui_titleBar"><div class="aui_title" style="cursor: move;"></div><a class="aui_close" href="javascript:/*artDialog*/;">×</a></div></td></tr><tr><td class="aui_icon" style="display: none;"><div class="aui_iconBg" style="background: none;"></div></td><td class="aui_main" style="width: auto; height: auto;"><div class="aui_content" style="padding: 20px 25px;"></div></td></tr><tr><td colspan="2" class="aui_footer"><div class="aui_buttons" style="display: none;"></div></td></tr></tbody></table></div></td><td class="aui_e"></td></tr><tr><td class="aui_sw"></td><td class="aui_s"></td><td class="aui_se" style="cursor: se-resize;"></td></tr></tbody></table></div></div>
    <div id="container" class="container">
        <div id="header">
	<div class="head w1366head">
		<a class="head-logo fl" href="/" style="background: url(&quot;https://staticlive.douyucdn.cn/upload/signs/201703031609518839.png&quot;) left center no-repeat;"></a>

		<ul class="head-nav fl">
			<li class="fl index ">
				<a href="/">首页</a>
			</li>
			<li class="fl live current">
				<a href="/directory/all">直播</a>
			</li>
			<li class="fl assort ">
				<a href="/directory">分类</a>
                <i></i>
<div class="a-pop">
    <i></i>

    <div class="a-list">
                <h3>热门分类</h3>
        <ul class="btns">
                        <li><a target="_blank" class="btn" href="/directory/game/LOL">英雄联盟</a></li>
                                <li><a target="_blank" class="btn" href="/directory/game/How">炉石传说</a></li>
                                <li><a target="_blank" class="btn" href="/directory/game/DOTA2">DOTA2</a></li>
                                <li><a target="_blank" class="btn" href="/directory/game/TVgame">主机游戏</a></li>
                                <li><a target="_blank" class="btn" href="/directory/game/Overwatch">守望先锋</a></li>
                                <li><a target="_blank" class="btn" href="/directory/game/jdqs">绝地求生</a></li>
                            </ul>
                            <h3>玩家推荐</h3>
        <ul class="btns">
                                <li><a target="_blank" class="btn" href="/directory/game/ecy">二次元</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/FTG">格斗游戏</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/classic">怀旧游戏</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/MC">我的世界</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/wzry">王者荣耀</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/hszz">皇室战争</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/LRSZQ">狼人杀专区</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/DNF">DNF</a></li>
                                        <li><a target="_blank" class="btn" href="/directory/game/HW">户外</a></li>
                            </ul>
                    <div class="btn-all">
            <a target="_blank" href="/directory">全部&gt;&gt;</a>
        </div>
		<div class="assort-ad" data-dysign="1" style="position: relative;"><i class="sign-spec"></i><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=615790&amp;posid=1&amp;projid=2657" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709011339206861.jpg" style="display:block; width:100%; height:100%"></a></div>
    </div>
</div>            </li>
            <li class="fl funny ">
                <a href="http://wan.douyu.com" target="_blank">游戏</a>
                <span class="g_hot_icon"></span>

<i></i>
<div class="a-pop">
    <i></i>
    <div class="a-list">
        <h3>网游推荐</h3>
                <ul class="btns" data-type="webgame">
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/moyu/" data-id="5027" data-name="魔域永恒">
                        魔域永恒                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/lsqy/" data-id="5032" data-name="龙神契约">
                        龙神契约                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/dydr/" data-id="5020" data-name="斗鱼达人">
                        斗鱼达人                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/lycq/" data-id="5003" data-name="蓝月传奇">
                        蓝月传奇                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/sslj/" data-id="5031" data-name="三十六计">
                        三十六计                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="http://wan.douyu.com/sdyxz/" data-id="5033" data-name="射雕英雄传">
                        射雕英雄传                    </a>
                </li>
                    </ul>
                <div class="btn-all" data-type="webgame"><a target="_blank" href="http://wan.douyu.com/">全部&gt;&gt;</a></div>

                <h3>手游推荐</h3>
        <ul class="btns" data-type="mobilegame">
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1265" data-id="1265" data-name="神无月">
                        神无月                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1290" data-id="1290" data-name="我叫MT开荒团">
                        我叫MT开荒团                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1299" data-id="1299" data-name="名侦探柯南">
                        名侦探柯南                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1280" data-id="1280" data-name="仙剑奇侠传5">
                        仙剑奇侠传5                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1272" data-id="1272" data-name="太极熊猫3">
                        太极熊猫3                    </a>
                </li>
                            <li>
                    <a target="_blank" class="btn" href="/mobileGame/detail/1292" data-id="1292" data-name="英灵召唤师">
                        英灵召唤师                    </a>
                </li>
                    </ul>
        <div class="btn-all" data-type="mobilegame"><a target="_blank" href="/mobileGame/home">全部&gt;&gt;</a></div>
                <!-- 兼容旧代码 -->
        <div class="assort-ad sign_posid" data-sign_posid="2" id="sign_p_2" data-dysign="2" style="position: relative;"><i class="sign-spec"></i><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=616182&amp;posid=2&amp;projid=2648" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709151742289958.jpg" style="display:block; width:100%; height:100%"></a></div>
    </div>
</div>
            </li>
            <li class="fl yuba">
                <a href="http://yuba.douyu.com/" target="_blank">鱼吧</a>
            </li>
            <li class="fl wxr-menu status-hidden">
                <a href="javascript:;" target="_blank"></a>
                <span class="wxr-hot-icon"><img src=""></span>
            </li>
        </ul>

        <div class="head-oth fr">
            <div class="search-suggest-box hide"></div><div class="o-search fl">
                <input class="s-ipt fl" type="text" autocomplete="off" value="" id="suggest-search">
                <a class="s-ico fr" href="#">
                    <i class="icofont"></i>
                </a>
            <label for="suggest-search" class="search-hot-key">吴家三婶@万美汐</label><label class="search-placeholder" for="suggest-search">房间/主播/分类/视频</label></div>
            <div class="o-history fl hide">
                <span class="icofont h-ico"></span>
                <span class="h-txt">历史</span>
                <div class="h-pop">
                    <i></i>
                    <div class="h-load">
                        <img src="https://shark.douyucdn.cn/app/douyu/res/com/loading.gif">
                        <span>数据加载中...</span>
                    </div>
                    <div class="h-none">
                        <p class="n-tt">信息动态</p>
                        <p class="n-cn">
                            <img src="https://shark.douyucdn.cn/app/douyu/res/com/sg-cry.png?v=20161204" alt="">
                            <span>你的历史列表空空如也~</span>
                        </p>
                    </div>
                    <ul class="h-list">
                    </ul>
                    <div class="his-sign-cont" data-dysign="24" style="position: relative;"><i class="sign-spec"></i><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=616136&amp;posid=24&amp;projid=2648" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709141829192939.jpg" style="display:block; width:100%; height:100%"></a></div>
                </div>
            </div>
            <div class="o-follow fl hide">
                <span class="icofont f-ico"></span>
                <span class="f-txt">关注</span>
                <div class="f-pop">
                    <i></i>
                    <div class="f-load">
                        <img src="https://shark.douyucdn.cn/app/douyu/res/com/loading.gif">
                        <span>数据加载中...</span>
                    </div>
                    <div class="f-none">
                        <p class="n-tt">信息动态</p>
                        <p class="n-cn">
                            <img src="https://shark.douyucdn.cn/app/douyu/res/com/sg-cry.png?v=20161204" alt="">
                            <span>你的关注列表空空如也~</span>
                        </p>
                    </div>
                    <ul class="f-list">
                    </ul>
                    <p class="f-all">
                        <a href="/room/my_follow">查看全部</a>
                    </p>
                    <div class="f-sign-cont" data-dysign="23" style="position: relative;"><i class="sign-spec"></i><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=616135&amp;posid=23&amp;projid=2648" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709141828382518.jpg" style="display:block; width:100%; height:100%"></a></div>
                </div>
            </div>
			<div class="o-download fl">
                <a href="/client?platform=0" target="_blank">
    				<span class="icofont d-ico"></span>
                    <span class="d-txt">下载</span>
                </a>
                <i></i>
                <div class="d-list">
                	<i></i>
                	<ul>
                      	<li>
                      		<a href="/client?platform=2" target="_blank">App下载</a>
                      	</li>
                        <li>
                            <a href="/client?platform=3" target="_blank">PC客户端下载</a>
                        </li>
                      	<li>
                      		<a href="/client?platform=1" target="_blank">主播工具下载</a>
                      	</li>
                  	</ul>
                </div>
			</div><div class="fl header-video-area"><a class="header-my-video" target="_blank" href="https://v.douyu.com"><span class="icon"></span><span>斗鱼视频</span><span class="video-msg-num"></span></a><div class="pop-dialog video-msg-pop"><div class="pop-arrow"></div><div class="pop-close">×</div><div class="cont"><div class="video-msg-list"></div></div></div><div class="pop-dialog header-video-guide " style="display: block;"><div class="pop-arrow"></div><div class="cont"><p class="strong">斗鱼短视频，想拍就拍！</p><p class="pop-paragraph">荣耀五杀时刻，主播翻车瞬间，美女花式尬舞，想拍就拍，玩的更High！</p><div class="pop-control"><a target="_blank" href="https://v.douyu.com/v/s" class="btn-yellow">去看看</a><div class="btn-white">朕知道了</div></div></div></div></div>
			<div class="o-unlogin fl">
				<span class="icofont u-ico fl"></span>
                <a class="u-login fl" href="/member/login" data-button-type="login">登录</a>
                <em class="fl">|</em>
                <a class="u-reg fl" href="/member/register" data-button-type="regis">注册</a>
			</div>
            <div class="o-login fl hide" data-login-content="yes">
                <a class="o-login-a" href="/member/cp" target="_blank">
				<span class="l-pic">
				</span>
                <span class="l-txt"> </span>
                </a>
                <i></i>
                <b class="hide umes-icon"></b>
                       <!-- l-menu -->
                <div class="l-menu">
                            <i class="lmsj-top"></i>
                            <div class="uinfo-dropmenu">
                                <div class="box1 chat-member">
                                    <div class="chat-mem-con clearfix">
                                        <div class="mem-pic">
                                            <a href="/member/cp" target="_blank" data-login-user="img-href">
                                                <img src="" data-login-user="header-img">
                                            </a>
                                            <!-- S 贵族图标 -->
                                            <img class="nobility-icon" src="" alt="贵族">
                                            <!-- E 贵族图标 -->
                                        </div>
                                        <div class="logname">
                                            <a class="name" data-login-user="user-name" href="/member/cp" target="_blank"></a>
                                            </div>
                                            <div class="authenticate">
                                            <a class="uname-aut"><i class="high"></i></a>
                                            <a class="mobile-aut"><i class="high"></i></a>
                                            <a class="email-aut"><i class="high"></i></a>
                                            </div>
                                        <div class="level-con clearfix">
                                            <a class="user-level user-level-loading" data-login-user="level-img" href="https://www.douyu.com/member/mylevel" target="_blank">
                                            </a>
                                            <a class="bar fl" href="/member/mylevel" target="_blank" data-exp-bar="btn">
                                                <div class="bar-per-wp">
                                                    <span class="bar-per" data-login-user="exp" style=""></span>
                                                </div>
                                                <span class="bar-num" data-login-user="exp-txt"></span>
                                                <div class="level-tip hide" data-exp-bar="box">
                                                    <p>
                                                        还需 <em data-login-user="up-exp-num"></em> 经验值到达下一级
                                                    </p>
                                                    <i></i>
                                                </div>
                                            </a>
                                            <a class="user-level-next user-level-loading" data-login-user="level-next-img" href="/member/mylevel" target="_blank">
                                            </a>
                                        </div>
                                        <a class="invisible is-invisible">进房间隐身
                                            <span class="invisible-sp">
                                                <i class="icon-invisible"></i>
                                                关闭进房间隐身
                                            </span>
                                            <span class="is-invisible-sp">
                                                <i class="icon-invisible"></i>
                                                开启隐身，隐藏进场信息
                                            </span>
                                        </a>
                                        <a class="logout" href="javascript:;">登出</a>
                                    </div>
                                </div>
                                <!-- S nobility-privilege-->
                                <div class="nobility-privilege">
                                    <!-- S 非贵族用户 -->

                                    <!-- E 非贵族用户 -->
                                </div>
                                <!-- E nobility-privilege-->
                                <!--wallet -->
                                <div class="box4 wallet">
                                    <div class="wallet-con clearfix">
                                        <div class="fl">
                                            <h2 class="title">我的钱包</h2>
                                            <div class="m-wealth">
                                                <span class="y1" title="做任务可获得鱼丸">鱼丸 <em data-login-user="silver"><img src="https://shark.douyucdn.cn/app/douyu/res/page/room-normal/loading.gif"></em></span>
                                                <span class="y2">鱼翅 <em data-login-user="gold"><img src="https://shark.douyucdn.cn/app/douyu/res/page/room-normal/loading.gif"></em></span>
                                                <!-- S 贵族鱼翅 -->
                                                <a class="y3" href="/member/noble/record" target="_blank">
                                                    (贵族鱼翅<em data-login-user="nobleGold"></em>)
                                                    <span class="y3-mask">
                                                        <i class="y3-mask-arrow"></i>
                                                        在贵族生效期间一直有效
                                                        <!-- <em data-login-user="ngdate"></em>-->
                                                    </span>
                                                </a>
                                                <!-- E 贵族鱼翅 -->
                                            </div>
                                        </div>
                                        <a class="r-com-btn getYc fr" href="/web_game/welcome/18" target="_blank">充值</a>
                                    </div>
                                </div>
                                <!--wallet -->
                                <!--task start-->
                                  <div class="box5 task clearfix">
                                    <h2 class="task-title">我的任务</h2>
                                    <div class="task-con">
                                        <a class="fl task-img task-a">

                                        </a>
                                        <div class="fl task-text">
                                            <a class="task-a clearfix"><h2 class="title"></h2></a>
                                            <p class="comment"></p>
                                        </div>
                                    </div>
                                </div>
                                <!--task end-->
                                <div class="box6 uim-foot">
                                    <ul class="clearfix">
                                        <li class="personal-center">
                                            <a href="/member" class="pc-a " target="_blank">
                                                <i></i>
                                                <p>个人中心</p>
                                            </a>
                       	</li>
                                        <li class="focus">
                                            <a href="/room/my_follow" class="focus-a " target="_blank">
                                                <i></i>
                                                <p>我的关注</p>
                                            </a>
                                        </li>
                                                                <li class="message">
                                            <a href="/member/pm" class="message-a " target="_blank">
                                                <i></i>
                                                <p>站内信</p>
                                                <b class="mes-icon hide"></b>
                                            </a>
                       	</li>
                                                                <li class="live-set">
                                            <a href="/room/my" class="live-set-a " target="_blank">
                                                <i></i>
                                                <em class="live-hot hide"></em>
                                                <p>直播设置</p>
                                            </a>
                        </li>
                    </ul>
                </div>
			</div>
		</div>
                        <!-- l-menu -->

	</div>
        </div>
    </div>
</div>        <div id="left" class="left-menu small" style="height: 813px;">
    <!-- 关闭按钮 -->
    <a class="left-btn">
        <span></span>
    </a>

    <!-- 导航展开状态 -->
    <div class="left-big">
        <div id="left-big-scroll" class="b-content" style="height: 813px;">
            <div class="scrollbar" style="height: 0px;">
                <div class="track" style="height: 0px;">
                    <div class="thumb" style="top: 0px; height: 506.848px;">
                        <div class="end"></div>
                    </div>
                </div>
            </div>
            <div class="viewport">
                <div class="overview" style="top: 0px;">
                    <!-- 四个大频道区域 -->
                    <div class="channel-cate">
                        <ul>
                            <li class="">
                                <a class="cur" href="/directory/all"> <i class="icon icon-live"></i>
                                    <span>全部直播</span>
                                </a>
                            </li>
                            <li class="">
                                <a href="/directory"> <i class="icon icon-game"></i>
                                    <span>全部分类</span>
                                </a>
                            </li>
                            <li class="rank">
                                <a href="/directory/rank_list/game" class="">
                                    <i class="icon icon-rank"></i>
                                    <span>排行榜</span>
                                </a>
                            </li>
                            <li class="follow">
                                <a href="/room/my_follow">
                                    <i class="icon icon-focus"></i>
                                    <span>我的关注</span>
                                </a>
                            </li>
                            <li>
                                <a href="http://wan.douyu.com/" target="_blank">
                                    <i class="icon icon-collect"></i>
                                    <span>页游中心</span>
                                                                        <i class="icon icon-hot"></i>                                </a>
                            </li>
                        </ul>
                    </div>

                    <!-- 游戏推荐区域 -->
                    <div class="leftnav-cate">
                        <div class="r-tit">
                            <ul>
                                <li class="cur">
                                    <i class="icon icon-column"></i>
                                    <span>栏目</span>
                                </li>
                                <li class="" data-item="发现">
                                    <i class="icon icon-recom"></i>
                                    <span>发现</span>
                                </li>
                            </ul>
                        </div>
                        <div class="r-cont column-cont ">
                            <dl>
                                <!--热门推荐分类-->
                                                                                                                                        <dt data-left-item="热门游戏">
                                    <a href="/directory/columnRoom/game" data-cid="1">
                                        <i></i><span>热门游戏</span>
                                    </a>
                                </dt>
                                <dd data-left-item="热门游戏">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/LOL" title="英雄联盟" data-tid="1">
                                                    英雄联盟                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/How" title="炉石传说" data-tid="2">
                                                    炉石传说                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/DOTA2" title="DOTA2" data-tid="3">
                                                    DOTA2                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/CF" title="穿越火线" data-tid="33">
                                                    穿越火线                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/MXD2" title="冒险岛2" data-tid="200">
                                                    冒险岛2                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/Overwatch" title="守望先锋" data-tid="148">
                                                    守望先锋                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/FTG" title="格斗游戏" data-tid="29">
                                                    格斗游戏                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/DNF" title="DNF" data-tid="40">
                                                    DNF                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/qipai" title="棋牌娱乐" data-tid="113">
                                                    棋牌娱乐                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/CSGO" title="CS:GO" data-tid="6">
                                                    CS:GO                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/mszb" title="魔兽争霸" data-tid="55">
                                                    魔兽争霸                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                                    <li>
                                                <a href="/directory/category/game" class="more">全部&gt;&gt;</a>
                                            </li>
                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="客厅游戏">
                                    <a href="/directory/columnRoom/ktyx" data-cid="15">
                                        <i></i><span>客厅游戏</span>
                                    </a>
                                </dt>
                                <dd data-left-item="客厅游戏">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/TVgame" title="主机游戏" data-tid="19">
                                                    主机游戏                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/jdqs" title="绝地求生" data-tid="270">
                                                    绝地求生                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/MC" title="我的世界" data-tid="44">
                                                    我的世界                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/classic" title="怀旧游戏" data-tid="26">
                                                    怀旧游戏                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/famine" title="饥荒" data-tid="23">
                                                    饥荒                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/zjyx" title="掌机游戏" data-tid="160">
                                                    掌机游戏                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/qrs" title="七日杀" data-tid="269">
                                                    七日杀                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                                    <li>
                                                <a href="/directory/category/ktyx" class="more">全部&gt;&gt;</a>
                                            </li>
                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="手游休闲">
                                    <a href="/directory/columnRoom/syxx" data-cid="9">
                                        <i></i><span>手游休闲</span>
                                    </a>
                                </dt>
                                <dd data-left-item="手游休闲">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/wzry" title="王者荣耀" data-tid="181">
                                                    王者荣耀                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/LRSZQ" title="狼人杀专区" data-tid="260">
                                                    狼人杀专区                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/yys" title="阴阳师" data-tid="240">
                                                    阴阳师                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/qzwz" title="CF手游" data-tid="178">
                                                    CF手游                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/xyzx" title="新游中心" data-tid="229">
                                                    新游中心                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/hyrz" title="火影忍者" data-tid="196">
                                                    火影忍者                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/ecysy" title="二次元手游" data-tid="254">
                                                    二次元手游                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/qqdzz" title="球球大作战" data-tid="192">
                                                    球球大作战                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                                    <li>
                                                <a href="/directory/category/syxx" class="more">全部&gt;&gt;</a>
                                            </li>
                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="娱乐">
                                    <a href="/directory/columnRoom/yl" data-cid="2">
                                        <i></i><span>娱乐</span>
                                    </a>
                                </dt>
                                <dd data-left-item="娱乐">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/yz" title="颜值" data-tid="201" class="current">
                                                    颜值                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/HW" title="户外" data-tid="124">
                                                    户外                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/xingyu" title="星娱" data-tid="287">
                                                    星娱                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/ms" title="美食" data-tid="194">
                                                    美食                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/music" title="音乐" data-tid="175">
                                                    音乐                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/ecy" title="二次元" data-tid="174">
                                                    二次元                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/ss" title="时尚" data-tid="159">
                                                    时尚                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                                    <li>
                                                <a href="/directory/category/yl" class="more">全部&gt;&gt;</a>
                                            </li>
                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="科技">
                                    <a href="/directory/columnRoom/kj" data-cid="3">
                                        <i></i><span>科技</span>
                                    </a>
                                </dt>
                                <dd data-left-item="科技">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/smkj" title="数码科技" data-tid="134">
                                                    数码科技                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/car" title="汽车" data-tid="136">
                                                    汽车                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/Finance" title="财经" data-tid="215">
                                                    财经                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/kepu" title="科普" data-tid="204">
                                                    科普                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/js" title="军事" data-tid="212">
                                                    军事                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                                    <li>
                                                <a href="/directory/category/kj" class="more">全部&gt;&gt;</a>
                                            </li>
                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="文娱课堂">
                                    <a href="/directory/columnRoom/wykt" data-cid="11">
                                        <i></i><span>文娱课堂</span>
                                    </a>
                                </dt>
                                <dd data-left-item="文娱课堂">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/yj" title="鱼教" data-tid="195">
                                                    鱼教                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/YY" title="鱼艺" data-tid="246">
                                                    鱼艺                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/stdp" title="视听点评" data-tid="208">
                                                    视听点评                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/qezb" title="企鹅直播" data-tid="207">
                                                    企鹅直播                                                </a>
                                            </li>
                                                                                <li>
                                                <a href="/directory/game/BLOVES" title="设计师" data-tid="283">
                                                    设计师                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->
                                                                                <li><a href="/directory/sport/cate" title="体育赛场">体育赛场</a></li>

                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                        <dt data-left-item="正能量">
                                    <a href="/directory/columnRoom/znl" data-cid="13">
                                        <i></i><span>正能量</span>
                                    </a>
                                </dt>
                                <dd data-left-item="正能量">
                                    <ul class="clearfix">

                                                                                    <li>
                                                <a href="/directory/game/znl" title="正能量" data-tid="250">
                                                    正能量                                                </a>
                                            </li>
                                                                        <!-- 添加固定企鹅栏目-->

                                                                            </ul>
                                </dd>
                                        <!--列表-->
                                                                                                </dl>

                        </div>
                        <div class="r-cont recom-cont hide">
                            <!-- 发现占位, 待替换 -->
                            <dl>
                                <dt data-left-item="我最喜欢" class="cur">
                                    <span>
                                        <i></i><span>我最喜欢</span>
                                    </span>
                                </dt>
                                <dd data-left-item="我最喜欢" data-tag_id="201" class="js-myfavorite-con">
                                    <ul class="clearfix">
                                    </ul>
                                </dd>

                                <!--鱼吧24H热帖-->
                                                                <dt data-left-item="24H热帖">
                                    <span>
                                        <i></i><span>24H热帖</span>
                                    </span>
                                </dt>
                                <dd data-left-item="24H热帖">
                                    <ol class="yb-list-24">
                                                                                                                                                                                                                    <li><span class="yb-num yb-num-1">1</span><a href="http://yuba.douyu.com/p/971921231500614190" target="_blank" title="【2017斗鱼绝地求生黄金赛】谁将带走最后的奖金？">【2017斗鱼绝地求生黄金赛】谁将带走最后的奖金？</a></li>
                                                                            </ol>
                                </dd>
                                                            </dl>
                            <!-- 发现占位, 待替换-END -->

                        </div>
                    </div>

                    <!-- 导航最底部 -->
                    <div class="left-footer">
                        <p class="f-line"></p>

                        <div class="btn-wrap">
                            <div class="btn-app">
                                <a href="/client" title="">
                                    <i class="icon icon-l"></i>
                                    <span>斗鱼APP</span>
                                </a>
                            </div>
                            <div class="btn-live">
                                <a href="/cms/zt/anchor_guide.html" title="我要直播">
                                    <i class="icon icon-l"></i>
                                    <span>我要直播</span>
                                </a>
                            </div>
                        </div>

                        <ul class="f-other clearfix">
                            <li><a href="/member/customer_service" target="_blank" title="直播指导">直播指导</a></li>
                            <li><a href="/member/customer_service" target="_blank" title="客服支持">客服支持</a></li>
                            <li><a href="http://jb.ccm.gov.cn/" target="_blank" title="房间举报">12318举报</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 导航收起状态 -->
    <div class="left-small">
        <div class="small-nav">
            <ul>
                <li>
                    <a href="/directory/all" title="直播" class=""> <i class="icon is1"></i>
                        <span>直播</span>
                    </a>
                </li>
                <li class="line"></li>
                <li>
                    <a href="/directory" title="分类" class=""> <i class="icon is2"></i>
                        <span>分类</span>
                    </a>
                </li>
                <li class="line"></li>
                <li class="rank">
                    <a href="/directory/rank_list/game" title="排行榜" class="">
                        <i class="icon icon-rank"></i>
                        <span>排行榜</span>
                    </a>
                </li>
                <li class="line"></li>
                <li class="follow">
                    <a href="/room/my_follow" title="关注" class="">
                        <i class="icon is3"></i>
                        <span>关注</span>
                    </a>
                </li>

                <li class="line"></li>
                <li>
                    <a title="游戏" target="_blank" href="http://wan.douyu.com/">
                        <i class="icon is4"></i>
                        <span>游戏</span>
                    </a>
                </li>
                <li class="line"></li>
            </ul>

            <div class="c-ser">
                <p class="line"></p>
                <div class="c-link">
                    <a href="/member/customer_service" target="_blank" title="客服">
                        <i class="cr_icon"></i>
                        <span>客服</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
        <div id="mainbody" style="height: 812px; margin-left: 76px;" class="w1366">

            <div class="expand-right column" id="main-col">
                <div class="content allList-cont">
                    <div class="tse-content padding-left0 padding-right0" style="display: block;">
                        <!-- web直播页广告位 -->
                                                    <div class="lol-ad">
                                <div class="two-img">
                                                                            <span class="fl dis" data-dysign="7" style="position: relative;"><i class="sign-spec"></i><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=616178&amp;posid=7&amp;projid=2648" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709151738421903.jpg" style="display: block; width: 100%; height: 100%;" src="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709151738421903.jpg"></a></span>

                                                                            <span class="fr dis" data-dysign="8"><a href="/lapi/sign/signapi/click?roomid=0&amp;aid=615701&amp;posid=8&amp;projid=2360" target="_blank"><img data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/08/201708301022416939.jpg" style="display: block; width: 100%; height: 100%;" src="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/08/201708301022416939.jpg"></a></span>
                                                                    </div>
                            </div>
                                                <!--新秀换一换开始 -->
                                                <!--新秀结束-->
                        <div class="player-column player_zb ">
                            <!-- 列表页分区定制化  begin -->
                                                    <!-- 列表页分区定制化 end -->
                                                        <div class="editable editable01 broadcast-meta">
                                                            <div class="rank-video"><div class="rank-video-ad fl" style="position: relative; display: block;"><a href="http://g.wan.douyu.com/s/1/1259/237.html?frm=sy-lb-tips" target="_blank"><img src="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/signs/2017/09/201709141821492684.png" style="width:100px;height:26px"></a></div>

                                        <a href="/directory/rank_list/yz" class="rank-video-item catagory-rank-btn" data-tid="201" data-cid="8">分区排行榜</a>
                                        <!--                                        <ul class="catagory-live-rank clearfix">-->
                                        <!--                                            <li class="catagory-rank "><a href="/directory/rank_list/--><!--">排行榜</a></li>-->
                                        <!--                                        </ul>-->

                                </div>

                                <div class="info padding-left0">
                                    <div class="title">
                                        <div class="real-title js-title alllive" style="float: none;">
                                                                                            <span>颜值</span>
                                                                                    </div>

                                                                                                                                        <div class="item_tag" id="js_item_tag">
                                                    <div class="tag_list">
                                                        <ul>
                                                            <li>
                                                                <a href="#" data-href="/directory/game/yz" data-pagecount="3" data-live-list-type="all" class="lihover">
                                                                全部
                                                                </a>
                                                            </li>
                                                                                                                    <li>
                                                                <a href="#" data-href="/directory/subCate/yz/544" data-pagecount="1" data-live-list-type="好声音" data-cid="8" data-tid="201" data-sid="544" class="">
                                                                    好声音                                                                </a>
                                                            </li>
                                                                                                                    <li>
                                                                <a href="#" data-href="/directory/subCate/yz/545" data-pagecount="2" data-live-list-type="新人" data-cid="8" data-tid="201" data-sid="545" class="">
                                                                    新人                                                                </a>
                                                            </li>
                                                                                                                    <li>
                                                                <a href="#" data-href="/directory/subCate/yz/546" data-pagecount="1" data-live-list-type="性感舞娘" data-cid="8" data-tid="201" data-sid="546" class="">
                                                                    性感舞娘                                                                </a>
                                                            </li>
                                                                                                                    <li>
                                                                <a href="#" data-href="/directory/subCate/yz/581" data-pagecount="1" data-live-list-type="聊天交友" data-cid="8" data-tid="201" data-sid="581" class="">
                                                                    聊天交友                                                                </a>
                                                            </li>
                                                                                                                </ul>
                                                    </div>
                                                </div>
                                                                                                                            <!-- 排行榜 -->

<!--                                        --><!--                                            <ul class="catagory-live-rank clearfix">-->
<!--                                                <li class="catagory-rank "><a href="/directory/rank_list/--><!--">排行榜</a></li>-->
<!--                                            </ul>-->
<!--                                        -->
                                        <!-- 排行榜end -->
                                        </div>
                                        <div class="titlebotborder">
                                            <div class="border1"></div>
                                            <div class="border2"></div>
                                        </div>
                                        <div class="titlebotbordermore" style="display: none;">
                                            <div class="border2">
                                                <div class="line" style="display: none;"></div>
                                                <a href="javascript:void(0);" id="tag_open_btn" style="display: none;">
                                                    <div class="wrap"><span>更多<i></i></span></div>

                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                                                            <div id="live-list-content" class="items items01 item-data clearfix">
                                    <ul id="live-list-contentbox" class="clearfix play-list x2">
                                                                                                            <li class="" data-ordertype="19" data-cid="8" data-rid="1970403" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1970403" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1970403" title="户外老城溜达溜达~" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/06/1970403_20170906132555_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/06/1970403_20170906132555_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        户外老城溜达溜达~                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小果汁hyr</span>
                                                <span class="dy-num fr">4067</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="19" data-cid="8" data-rid="924562" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="924562" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/adzz" title="一次失败的cosplay" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/16/924562_20170916160857_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/16/924562_20170916160857_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        一次失败的cosplay                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">艾达啊Ada</span>
                                                <span class="dy-num fr">9923</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="19" data-cid="8" data-rid="827347" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="827347" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/827347" title="周末可以来看我吗" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/16/827347_20170916191643_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/16/827347_20170916191643_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        周末可以来看我吗                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">冷冷的喵喵喵</span>
                                                <span class="dy-num fr">3251</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="19" data-cid="8" data-rid="2455704" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2455704" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2455704" title="太阳当空照小姐姐对你笑" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2455704_20170917140806_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/17/2455704_20170917140806_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        太阳当空照小姐姐对你笑                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">舒妤lucky</span>
                                                <span class="dy-num fr">698</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="19" data-cid="8" data-rid="2219619" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2219619" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2219619" title="国民少女小水酱" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/28/2219619_20170828162041_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/08/28/2219619_20170828162041_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        国民少女小水酱                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">水水小水酱</span>
                                                <span class="dy-num fr">1296</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="19" data-cid="8" data-rid="2152830" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2152830" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/xumuqing" title="标题失踪啦，什么时候能回来？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/06/2152830_20170906130202_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/06/2152830_20170906130202_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        标题失踪啦，什么时候能回来？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">慕晴muqing</span>
                                                <span class="dy-num fr">2183</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="19" data-cid="8" data-rid="3250449" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3250449" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/3250449" title="我很温柔 也是浪漫的Hero" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/3250449_20170914185042_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/14/3250449_20170914185042_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        我很温柔 也是浪漫的Hero                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你的念奴菲儿</span>
                                                <span class="dy-num fr">1722</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="19" data-cid="8" data-rid="1501063" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1501063" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1501063" title="晚上1点波噢 等你哦" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/16/1501063_20170916201720_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/16/1501063_20170916201720_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        晚上1点波噢 等你哦                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">芭比感谢有你</span>
                                                <span class="dy-num fr">656</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="19" data-cid="8" data-rid="754624" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="754624" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/754624" title="新主播求关注哦ii" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/08/754624_20170908150803_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/08/754624_20170908150803_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新主播求关注哦ii                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">叫我呢喃就好</span>
                                                <span class="dy-num fr">671</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="19" data-cid="2" data-rid="2987252" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2987252" data-tid="311" data-sid="0" data-rpos="0" data-sub_rt="0" href="/2987252" title="跳起舞来双脚离地" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/roomCover/2017/09/06/4ddd70c0379e2039f3f4e6adaa50c73c_small.jpg" src="https://rpic.douyucdn.cn/roomCover/2017/09/06/4ddd70c0379e2039f3f4e6adaa50c73c_small.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-pc">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        跳起舞来双脚离地                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">喵小仙欣宝</span>
                                                <span class="dy-num fr">151</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="20" data-cid="8" data-rid="984069" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="984069" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/Aaya" title="这里是MC瞎bb的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/23/984069_20170823192629_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/08/23/984069_20170823192629_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        这里是MC瞎bb的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">帅气迷人的王思川</span>
                                                <span class="dy-num fr">1571</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="20" data-cid="8" data-rid="2002312" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2002312" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2002312" title="脾气小凶，生人勿投食" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/2002312_20170909174223_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/09/2002312_20170909174223_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        脾气小凶，生人勿投食                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">大木头CL</span>
                                                <span class="dy-num fr">1593</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="20" data-cid="8" data-rid="2449973" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2449973" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2449973" title="声乐课 求关注 守护" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/2449973_20170909170239_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/09/2449973_20170909170239_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        声乐课 求关注 守护                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Wuli伊凡</span>
                                                <span class="dy-num fr">1421</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="20" data-cid="8" data-rid="3031035" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3031035" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3031035" title="爱情运在哪里" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/3031035_20170914025506_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/14/3031035_20170914025506_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        爱情运在哪里                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">子雯bb</span>
                                                <span class="dy-num fr">1353</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="20" data-cid="8" data-rid="3226340" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3226340" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3226340" title="曲奇奇奇奇xq的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3226340_20170915184759_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/15/3226340_20170915184759_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        曲奇奇奇奇xq的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">曲奇奇奇奇xq</span>
                                                <span class="dy-num fr">20</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="20" data-cid="8" data-rid="2109881" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2109881" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2109881" title="女神姐姐又回来了" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/16/2109881_20170916192525_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/16/2109881_20170916192525_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        女神姐姐又回来了                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">紫絮儿521</span>
                                                <span class="dy-num fr">1146</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="20" data-cid="8" data-rid="3107376" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3107376" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/3107376" title="SK大树君儿的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/31/3107376_20170831175454_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/08/31/3107376_20170831175454_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        SK大树君儿的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">SK大树君儿</span>
                                                <span class="dy-num fr">27</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="20" data-cid="8" data-rid="2195134" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2195134" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2195134" title="距离你……1米" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2195134_20170917160017_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/17/2195134_20170917160017_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        距离你……1米                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你的泡沫呀</span>
                                                <span class="dy-num fr">20</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1047629" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1047629" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1047629" title="运动风？会不会很傻？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/22/1047629_20170822185419_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/08/22/1047629_20170822185419_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        运动风？会不会很傻？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Piano小詩</span>
                                                <span class="dy-num fr">7181</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="1111421" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1111421" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1111421" title="可爱宥迷人的反派角色♥" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/1111421_20170915183043_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/15/1111421_20170915183043_big.jpg" width="283" height="163" style="display: block;">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        可爱宥迷人的反派角色♥                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">宥唯</span>
                                                <span class="dy-num fr">1453</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="1578588" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1578588" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1578588" title="四点见哟～嘻嘻" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/07/1578588_20170807212239_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        四点见哟～嘻嘻                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">皇甫旭娜</span>
                                                <span class="dy-num fr">512</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2136878" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2136878" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2136878" title="昂，生病呐，等我满血肥来哦！！！" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/28/2136878_20170828222948_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        昂，生病呐，等我满血肥来哦！！！                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Zz仔仔呐</span>
                                                <span class="dy-num fr">5506</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="822764" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="822764" data-tid="201" data-sid="546" data-rpos="0" data-sub_rt="0" href="/822764" title="你听话就不拷你(万圣节系列)" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/822764_20170915175931_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        你听话就不拷你(万圣节系列)                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">巫女蛋</span>
                                                <span class="dy-num fr">8031</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="1089201" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1089201" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1089201" title="十个人的大主播就是我啦啦" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/06/1089201_20170906180418_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        十个人的大主播就是我啦啦                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">爱打嗝的璐Dad</span>
                                                <span class="dy-num fr">391</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="469479" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="469479" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/469479" title="我的小可爱，皇冠给我戴" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>

                                            <i class="icon_lottery"></i>

                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/469479_20170915005625_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        我的小可爱，皇冠给我戴                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">谢谢小小七</span>
                                                <span class="dy-num fr">1650</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2555564" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2555564" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2555564" title="琵琶《一生所爱》" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/07/2555564_20170907164155_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        琵琶《一生所爱》                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">摔倒的小软妹l</span>
                                                <span class="dy-num fr">223</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="2" data-rid="2915698" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2915698" data-tid="311" data-sid="0" data-rpos="0" data-sub_rt="0" href="/2915698" title="温柔又粗暴的小可" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/roomCover/2017/08/15/6273b3faca831db752786578431b6d85_small.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-pc">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        温柔又粗暴的小可                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">kris小可</span>
                                                <span class="dy-num fr">293</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="2228385" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2228385" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2228385" title="日常忙里偷闲看兔兔❤️" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/10/2228385_20170910135537_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        日常忙里偷闲看兔兔❤️                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">谢小兔兔兔</span>
                                                <span class="dy-num fr">2969</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2426476" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2426476" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2426476" title="老铁 飙车 来啊？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/26/2426476_20170826195237_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        老铁 飙车 来啊？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你的小祖宗来啦</span>
                                                <span class="dy-num fr">824</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2623238" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2623238" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2623238" title="新人求关注⁉️你是对的我是错的" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/22/2623238_20170822192444_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新人求关注⁉️你是对的我是错的                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">痣哥呦妹</span>
                                                <span class="dy-num fr">65</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1147493" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1147493" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1147493" title="薇薇说你很迷人但我得回家" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/1147493_20170914233509_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        薇薇说你很迷人但我得回家                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">薇薇小baby</span>
                                                <span class="dy-num fr">113</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="1855155" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1855155" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1855155" title="跳过来就是一个么么哒" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/1855155_20170909184548_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        跳过来就是一个么么哒                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">安安爱吃小桔子</span>
                                                <span class="dy-num fr">2311</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="3224999" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3224999" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3224999" title="小瑶瑶Cherry的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3224999_20170915140451_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        小瑶瑶Cherry的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小瑶瑶Cherry</span>
                                                <span class="dy-num fr">831</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1272264" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1272264" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1272264" title="上声乐课。。。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/21/1272264_20170821121256_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        上声乐课。。。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">菁菁Krystal</span>
                                                <span class="dy-num fr">2814</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2554845" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2554845" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2554845" title="主播的牙齿会放光" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/2554845_20170914140136_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        主播的牙齿会放光                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">玛丽莲小萌璐</span>
                                                <span class="dy-num fr">99</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="2591083" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2591083" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2591083" title="爱唱歌的大柚子" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/12/2591083_20170912202555_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        爱唱歌的大柚子                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">柚子nancy</span>
                                                <span class="dy-num fr">92</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3156748" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3156748" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3156748" title="悠悠的我，你的悠悠" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/3156748_20170913175946_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        悠悠的我，你的悠悠                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">lee悠悠</span>
                                                <span class="dy-num fr">97</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3030605" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3030605" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/3030605" title="是不是你最疼爱的人" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3030605_20170915004314_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        是不是你最疼爱的人                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">雯槿是只小绵羊</span>
                                                <span class="dy-num fr">114</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2481554" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2481554" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2481554" title="岁月漫长 要心地善良" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/2481554_20170915225948_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        岁月漫长 要心地善良                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">懵逼的大花猫</span>
                                                <span class="dy-num fr">119</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="3018607" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3018607" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3018607" title="星期天都放假啦！来玩！" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/28/3018607_20170828214317_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        星期天都放假啦！来玩！                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你滴女孩彤宝</span>
                                                <span class="dy-num fr">630</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2458672" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2458672" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2458672" title="卖血哥的小迷妹，哇呜✔" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/2458672_20170914203526_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        卖血哥的小迷妹，哇呜✔                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Sunny小贝儿</span>
                                                <span class="dy-num fr">170</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="833314" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="833314" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/833314" title="今天下午可准时了哦！需要表扬" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/10/833314_20170910162601_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        今天下午可准时了哦！需要表扬                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">兰兰丫</span>
                                                <span class="dy-num fr">2226</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2820810" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2820810" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2820810" title="嘟嘟嘟。。。上车了。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2820810_20170917121049_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        嘟嘟嘟。。。上车了。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Ti丶熙熙</span>
                                                <span class="dy-num fr">604</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="3106047" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3106047" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/3106047" title="hello妮可的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/04/3106047_20170904192645_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        hello妮可的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">hello妮可</span>
                                                <span class="dy-num fr">131</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2694688" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2694688" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2694688" title="小兮兮拉拉" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2694688_20170917135834_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        小兮兮拉拉                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">沐兮兮万岁</span>
                                                <span class="dy-num fr">2245</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2754690" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2754690" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2754690" title="个人主播，不签约，没才艺，套路很深" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/08/2754690_20170908171054_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        个人主播，不签约，没才艺，套路很深                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">wo屿凉</span>
                                                <span class="dy-num fr">129</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1869428" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1869428" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1869428" title="新主播开播啦！" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/11/1869428_20170911143710_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新主播开播啦！                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">桃桃心心心</span>
                                                <span class="dy-num fr">152</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="1676220" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1676220" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1676220" title="来聊天呀~快来快来" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/05/01/1676220_20170501120629_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        来聊天呀~快来快来                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">TwinsBabyMJ</span>
                                                <span class="dy-num fr">2340</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2484765" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2484765" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2484765" title="来听我的演唱会*\(^o^)/*" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/2484765_20170915171958_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        来听我的演唱会*\(^o^)/*                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">育美小姐姐</span>
                                                <span class="dy-num fr">166</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2312445" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2312445" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2312445" title="我有猫咪，有音乐，还有你们。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/21/2312445_20170821010757_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        我有猫咪，有音乐，还有你们。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">尹晗YH</span>
                                                <span class="dy-num fr">861</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2118061" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2118061" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2118061" title="新人主播求关注＝3＝❤️" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/31/2118061_20170731213602_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新人主播求关注＝3＝❤️                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">大米饭诶</span>
                                                <span class="dy-num fr">1254</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="1264973" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1264973" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1264973" title="乔儿：喜欢你们拿我当BGM" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/06/19/1264973_20170619174537_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        乔儿：喜欢你们拿我当BGM                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">乔儿儿儿儿儿</span>
                                                <span class="dy-num fr">909</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2542184" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2542184" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2542184" title="要好好学习啊" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2542184_20170917143626_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        要好好学习啊                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">抹茶味的二狗</span>
                                                <span class="dy-num fr">2482</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2134370" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2134370" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2134370" title="回武汉啦啦啦啦" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/03/2134370_20170703164321_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        回武汉啦啦啦啦                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">水果莎拉呀</span>
                                                <span class="dy-num fr">1403</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2297285" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2297285" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2297285" title="一见如故容易，难的是来日方长的陪伴" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/28/2297285_20170728181702_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        一见如故容易，难的是来日方长的陪伴                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">神宠桃大头</span>
                                                <span class="dy-num fr">1148</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="868861" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="868861" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/868861" title="爱笑的人～运气不会差吧" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/29/868861_20170829173956_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        爱笑的人～运气不会差吧                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">三碎碎</span>
                                                <span class="dy-num fr">2324</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2325754" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2325754" data-tid="201" data-sid="546" data-rpos="0" data-sub_rt="0" href="/2325754" title="我是一个磨人的小仙女" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/06/2325754_20170806175732_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        我是一个磨人的小仙女                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">CoCo熙妍</span>
                                                <span class="dy-num fr">1092</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="2" data-rid="172549" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="172549" data-tid="311" data-sid="0" data-rpos="0" data-sub_rt="0" href="/Lxx13" title="唱什么好呢" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/roomCover/2017/09/12/8595aaa5d11de1e795c67c081fb2e19c_small.png" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-pc">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        唱什么好呢                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">璇璇璇儿丶Tay</span>
                                                <span class="dy-num fr">127</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1416006" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1416006" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1416006" title="超级大额头" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/21/1416006_20170821145726_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        超级大额头                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小污神mm</span>
                                                <span class="dy-num fr">1064</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="2358041" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2358041" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2358041" title="饿。。我先吃为敬～" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/2358041_20170913005713_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        饿。。我先吃为敬～                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小圆脸静静</span>
                                                <span class="dy-num fr">723</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2678441" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2678441" data-tid="201" data-sid="546" data-rpos="0" data-sub_rt="0" href="/2678441" title="主播提到了你" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/2678441_20170915214224_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        主播提到了你                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">朵朵是仙女啊</span>
                                                <span class="dy-num fr">816</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2844641" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2844641" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2844641" title="哥哥，你要来陪乔气玩吗？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/2844641_20170909231847_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        哥哥，你要来陪乔气玩吗？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">乔气鬼</span>
                                                <span class="dy-num fr">560</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2461018" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2461018" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2461018" title="biubiubiu～～～." target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/05/2461018_20170905235926_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        biubiubiu～～～.                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">阿狸小公主丶</span>
                                                <span class="dy-num fr">99</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="2" data-rid="630154" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="630154" data-tid="311" data-sid="0" data-rpos="0" data-sub_rt="0" href="/630154" title="嗨，我是虾米儿" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/09/630154_20170809181635_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-pc">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        嗨，我是虾米儿                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">虾米是个小仙女</span>
                                                <span class="dy-num fr">78</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1432751" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1432751" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1432751" title="聊会天唱唱歌" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/roomCover/mixed_stream/2017/09/17/170917162428_1432751_5f75611af7873f7d307edfb32097f485.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        聊会天唱唱歌                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">我要吃你豆腐丶欢畅</span>
                                                <span class="dy-num fr">2256</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2610485" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2610485" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2610485" title="赖懒懒bbbb的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/19/2610485_20170719154223_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        赖懒懒bbbb的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">赖懒懒bbbb</span>
                                                <span class="dy-num fr">99</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2937317" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2937317" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2937317" title="阮糖GX很甜的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/17/2937317_20170817174845_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        阮糖GX很甜的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">阮糖GX很甜</span>
                                                <span class="dy-num fr">590</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="3025194" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3025194" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3025194" title="你喜欢的样子我都有~" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/3025194_20170909233926_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        你喜欢的样子我都有~                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Janna诺</span>
                                                <span class="dy-num fr">17</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="1457528" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1457528" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1457528" title="我来自长沙，你来自哪里。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/10/1457528_20170910105721_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        我来自长沙，你来自哪里。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Vv子教授</span>
                                                <span class="dy-num fr">59</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="464105" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="464105" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/464105" title="初次见面，请多关照呀" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/25/464105_20170825180345_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        初次见面，请多关照呀                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">唐唐不吃糖i</span>
                                                <span class="dy-num fr">2674</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2736845" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2736845" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2736845" title="小露露求升级" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/11/2736845_20170911191854_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        小露露求升级                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">anzulu露露</span>
                                                <span class="dy-num fr">173</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="2174311" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2174311" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2174311" title="你会不会突然的出现～" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/2174311_20170915224635_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        你会不会突然的出现～                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">是笑笑丶</span>
                                                <span class="dy-num fr">2246</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2821681" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2821681" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2821681" title="保护我方馨宝儿的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/08/2821681_20170808155848_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        保护我方馨宝儿的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">保护我方馨宝儿</span>
                                                <span class="dy-num fr">69</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1614152" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1614152" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1614152" title="播会。。。。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/1614152_20170913115614_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        播会。。。。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">大倩倩欧尼酱</span>
                                                <span class="dy-num fr">2327</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2024545" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2024545" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2024545" title="唱个歌儿^_^新人求关注" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2024545_20170917134626_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        唱个歌儿^_^新人求关注                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你的阿轲</span>
                                                <span class="dy-num fr">2194</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="2977077" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2977077" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2977077" title="是你掉的小可爱吗~？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/30/2977077_20170830185842_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        是你掉的小可爱吗~？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">秋山染</span>
                                                <span class="dy-num fr">14</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3093198" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3093198" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/3093198" title="不知马力的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3093198_20170915152133_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        不知马力的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">不知马力</span>
                                                <span class="dy-num fr">68</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2492440" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2492440" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2492440" title="畅游苏梅岛wuho～" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/11/2492440_20170811180709_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        畅游苏梅岛wuho～                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">罗十三VIVI</span>
                                                <span class="dy-num fr">1161</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2210827" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2210827" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2210827" title="没人扶你的时候 自己要站直 路还长 背影要美" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/06/2210827_20170906134337_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        没人扶你的时候 自己要站直 路还长 背影要美                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">DJ美人颜</span>
                                                <span class="dy-num fr">550</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="3252796" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3252796" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3252796" title="终结者大长腿" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3252796_20170915143217_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        终结者大长腿                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">女士大长腿</span>
                                                <span class="dy-num fr">571</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="1492452" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1492452" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1492452" title="不来看看小姐姐吗~" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/25/1492452_20170825004631_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        不来看看小姐姐吗~                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">没有糖也很甜的ANNA</span>
                                                <span class="dy-num fr">38</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2438319" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2438319" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2438319" title="如果思念有声音" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/30/2438319_20170830140629_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        如果思念有声音                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">萌小萌兒丶</span>
                                                <span class="dy-num fr">1280</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="335219" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="335219" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/liuduoduo" title="拿我性别四下次不鸽了" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/11/335219_20170911151001_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        拿我性别四下次不鸽了                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">柳哆哆头上有两个坑</span>
                                                <span class="dy-num fr">1447</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="764793" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="764793" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/764793" title="第一次一個人⋯⋯嚶嚶嚶" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/09/764793_20170809142851_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        第一次一個人⋯⋯嚶嚶嚶                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小喬妹</span>
                                                <span class="dy-num fr">737</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1161765" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1161765" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1161765" title="呀 眼睛好疼" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/1161765_20170914110132_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        呀 眼睛好疼                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">特别涵babe</span>
                                                <span class="dy-num fr">459</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1205098" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1205098" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1205098" title="最美还是你们爱的我♥" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/12/1205098_20170912160921_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        最美还是你们爱的我♥                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Oh丶My迪兒</span>
                                                <span class="dy-num fr">1198</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="1497341" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1497341" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1497341" title="如果最后是你那么晚点也没关系" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/23/1497341_20170723201444_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        如果最后是你那么晚点也没关系                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">可爱christina</span>
                                                <span class="dy-num fr">314</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="1759075" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1759075" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1759075" title="美美的笑换你一个暖暖的关注。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/05/1759075_20170905201436_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        美美的笑换你一个暖暖的关注。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">罒小北</span>
                                                <span class="dy-num fr">374</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="1957735" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1957735" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1957735" title="你好，我是77~" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/21/1957735_20170821221342_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        你好，我是77~                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">77琪琪酱</span>
                                                <span class="dy-num fr">69</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2196994" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2196994" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2196994" title="晚点遇到你，余生全是你" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/06/13/2196994_20170613212025_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        晚点遇到你，余生全是你                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Daisy李艾米</span>
                                                <span class="dy-num fr">195</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2491730" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2491730" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2491730" title="看一下，万一你看着顺眼呢" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/14/2491730_20170914191048_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        看一下，万一你看着顺眼呢                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">欲罢不能的小饼干</span>
                                                <span class="dy-num fr">1427</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="2678501" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2678501" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2678501" title="小珺说人无完人" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/26/2678501_20170726144330_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        小珺说人无完人                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小珺Baby</span>
                                                <span class="dy-num fr">1215</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="2747379" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2747379" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2747379" title="今天播一会" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/17/2747379_20170817220155_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        今天播一会                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">丶薄荷姑娘Mint</span>
                                                <span class="dy-num fr">126</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2759653" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2759653" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2759653" title="来听歌吧^O^" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/04/2759653_20170804210616_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        来听歌吧^O^                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">你的小小甜</span>
                                                <span class="dy-num fr">7</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="2840000" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2840000" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2840000" title="叫我奈奈呀" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/08/2840000_20170908190008_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        叫我奈奈呀                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">叫我奈奈呀</span>
                                                <span class="dy-num fr">51</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="11" data-cid="8" data-rid="2871148" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2871148" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2871148" title="新设备到啦哈哈哈" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/2871148_20170915123259_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新设备到啦哈哈哈                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">奥利o奥</span>
                                                <span class="dy-num fr">20</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3006667" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3006667" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3006667" title="每天我都在这里等你:你会来吗？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/3006667_20170917094525_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        每天我都在这里等你:你会来吗？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">安然Luck</span>
                                                <span class="dy-num fr">20</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3024716" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3024716" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3024716" title="新人小屁孩" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/31/3024716_20170831122401_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        新人小屁孩                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">芷若秋殇</span>
                                                <span class="dy-num fr">0</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="11" data-cid="8" data-rid="3080815" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3080815" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/3080815" title="艾艾小迷糊的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/roomCover/2017/08/29/1f9f4fda8a3a9c5c7dff9c3215c8d50d_small.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        艾艾小迷糊的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">艾艾小迷糊</span>
                                                <span class="dy-num fr">9</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="11" data-cid="8" data-rid="3080831" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3080831" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3080831" title="JoJo北鼻听说像宋佳？" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/11/3080831_20170911032743_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        JoJo北鼻听说像宋佳？                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">JoJo北鼻</span>
                                                <span class="dy-num fr">57</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="11" data-cid="8" data-rid="3226943" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3226943" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/3226943" title="来尬聊啊兄弟们" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/15/3226943_20170915184409_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        来尬聊啊兄弟们                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">家養貓</span>
                                                <span class="dy-num fr">150</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="10" data-cid="8" data-rid="1727410" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1727410" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1727410" title="岁月无处不在 瓜皮随时替代" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/19/1727410_20170819211639_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        岁月无处不在 瓜皮随时替代                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">女孩子味的小草莓a</span>
                                                <span class="dy-num fr">242</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="2068014" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2068014" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/2068014" title="寻求守护小哥哥" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/21/2068014_20170821214435_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        寻求守护小哥哥                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">啦啦laura</span>
                                                <span class="dy-num fr">612</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="10" data-cid="8" data-rid="3057815" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3057815" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3057815" title="傻傻新主播、求带求关注、老司机带带我…" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/28/3057815_20170828174655_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        傻傻新主播、求带求关注、老司机带带我…                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">璃儿丶璃儿吖</span>
                                                <span class="dy-num fr">788</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="10" data-cid="8" data-rid="3085950" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3085950" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3085950" title="好像没人……" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/3085950_20170909032226_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        好像没人……                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">浪浪浪葩云儿</span>
                                                <span class="dy-num fr">258</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="2271118" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2271118" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2271118" title="周末在家懒" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/09/2271118_20170709153358_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        周末在家懒                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">許小吱hsu</span>
                                                <span class="dy-num fr">30</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="3216095" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3216095" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3216095" title="大家都吃完饭了不" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/3216095_20170913125455_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        大家都吃完饭了不                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Jessie小碗</span>
                                                <span class="dy-num fr">19</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="10" data-cid="8" data-rid="1231616" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1231616" data-tid="201" data-sid="544" data-rpos="0" data-sub_rt="0" href="/1231616" title="哈哈恭喜发财恭喜发财。" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/22/1231616_20170722172834_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        哈哈恭喜发财恭喜发财。                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">洛小饵</span>
                                                <span class="dy-num fr">1315</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="3195312" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3195312" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3195312" title="小茹哥哥er的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/11/3195312_20170911154236_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        小茹哥哥er的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">小茹哥哥er</span>
                                                <span class="dy-num fr">20</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="1187852" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1187852" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/1187852" title="兔兔:(⊙o⊙)…呃呃呃额额" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/15/1187852_20170815032154_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        兔兔:(⊙o⊙)…呃呃呃额额                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">珊儿兔兔兔</span>
                                                <span class="dy-num fr">131</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="10" data-cid="8" data-rid="2439468" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2439468" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2439468" title="当一个安静的小仙女" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/01/2439468_20170801233924_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        当一个安静的小仙女                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">CCChuChu</span>
                                                <span class="dy-num fr">63</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="10" data-cid="8" data-rid="2898728" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2898728" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2898728" title="给六岁办张卡买糖吃～" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/2898728_20170917140832_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        给六岁办张卡买糖吃～                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">哼叽六岁</span>
                                                <span class="dy-num fr">60</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="1863865" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="1863865" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/1863865" title="庆幸有你爱我" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/12/1863865_20170912165537_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        庆幸有你爱我                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">F罩平胸婷</span>
                                                <span class="dy-num fr">8</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="10" data-cid="8" data-rid="2572605" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2572605" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2572605" title="感冒不想跳舞的小仙女" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/04/2572605_20170904143123_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        感冒不想跳舞的小仙女                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">Mr君先森</span>
                                                <span class="dy-num fr">2265</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="2357287" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2357287" data-tid="201" data-sid="581" data-rpos="0" data-sub_rt="0" href="/2357287" title="午夜音乐陪伴你入睡" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/07/10/2357287_20170710095924_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        午夜音乐陪伴你入睡                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">G奶小6</span>
                                                <span class="dy-num fr">55</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="last" data-ordertype="10" data-cid="8" data-rid="3154362" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3154362" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3154362" title="大長腿要人氣UP↑↑↑" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/3154362_20170913014224_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        大長腿要人氣UP↑↑↑                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">自欣kina</span>
                                                <span class="dy-num fr">11</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="serach_lastli" data-ordertype="10" data-cid="8" data-rid="3000068" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3000068" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3000068" title="发呆可以吗" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/08/31/3000068_20170831232044_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        发呆可以吗                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">啊梦是胖纸</span>
                                                <span class="dy-num fr">71</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="3281633" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="3281633" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/3281633" title="辛颖颖的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/17/3281633_20170917120910_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        辛颖颖的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">辛颖颖</span>
                                                <span class="dy-num fr">11</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="" data-ordertype="10" data-cid="8" data-rid="2308153" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2308153" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2308153" title="MIKI:陪你到世界尽头" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/05/2308153_20170905194940_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        MIKI:陪你到世界尽头                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">MIKI琦琦大明星</span>
                                                <span class="dy-num fr">2058</span>
                                            </p>
                </div>
            </a>
        </li>
                        <li class="lastserach_lastli" data-ordertype="10" data-cid="8" data-rid="2543706" data-is-on="1" data-rpos="0" data-sub_rt="0" data-bid="0">
            <a class="play-list-link" data-rid="2543706" data-tid="201" data-sid="545" data-rpos="0" data-sub_rt="0" href="/2543706" title="钓鱼的女孩的直播间" target="_blank" data-bid="0">
                <span class="imgbox">
                    <span class="imgbox-corner-mark">



                                                                    </span>
                    <b></b>
                    <i class="black"></i>


                    <img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/09/2543706_20170909214915_big.jpg" src="https://shark.douyucdn.cn/app/douyu/res/page/list-item-def-rect-thumb.gif" width="283" height="163">
                                        <div class="live-device-wrap device-mobile">
                        <div class="live-device-icon"></div>
                    </div>
                                    </span>

                <div class="mes">
                    <div class="mes-tit">
                        <h3 class="ellipsis">
                                                        钓鱼的女孩的直播间                        </h3>
                        <span class="tag ellipsis">颜值</span>
                    </div>
                    <p>

                        <span class="dy-name ellipsis fl">钓鱼的女孩</span>
                                                <span class="dy-num fr">59</span>
                                            </p>
                </div>
            </a>
        </li>
                                                                                            </ul>
                                </div>
                                                                                        <div id="J-pager" class="tcd-page-code"> <a href="#" class="shark-pager-prev shark-pager-disable shark-pager-disable-prev">上一页</a><a href="#" class="shark-pager-item current">1</a><a href="#" class="shark-pager-item">2</a><a href="#" class="shark-pager-item">3</a><a href="#" class="shark-pager-next">下一页</a><span class="jumppage">跳转到：</span><input class="jumptxt" name="" type="text"><a href="#" class="shark-pager-submit">GO</a></div>
                                                    </div>
                    </div>
                </div>
                <div id="live-loading">
                    <img src="https://shark.douyucdn.cn//app/douyu/res/page/room-normal/loading.gif" alt="loading">
                </div>
            </div>

        </div>

        <script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/app/douyu-passport/js/page/sdk/douyu-user-sdk.js?nv=v6.887"></script>
<script id="dytemp-loginpop-shadow" type="douyu/template">
    <div class="login-pop-shadow hide"></div>
</script>

<script id="dytemp-vcode9-shadow" type="douyu/template">
    <div class="vcode9-shadow hide"></div>
</script>

<script id="dytemp-vcode9" type="douyu/template">
    <div class="vcode9" data-src="/member/register/regcaptcha">
        <div class="vcode9-tit clearfix">
            <h3>输入验证码完成注册</h3>
            <a href="#" class="vcode9-close">关闭</a>
        </div>

        <div class="vcode9-con">
            <div class="vcode9-preview clearfix">
                <span>验证码</span>
                <b></b>
                <b></b>
                <b></b>
                <b></b>
                <b class="p-delete" title="清除"></b>
            </div>
            <div class="vcode9-guide">
                <span></span>
                <a href="#">看不清？</a>
            </div>
            <div class="vcode9-action">点击框内文字输入验证码</div>
            <div class="vcode9-input clearfix">
                <a class="i-0" href="#">
                    <b data-num="0"></b>
                </a>
                <a class="i-1" href="#">
                    <b data-num="1"></b>
                </a>
                <a class="i-2" href="#">
                    <b data-num="2"></b>
                </a>
                <a class="i-3" href="#">
                    <b data-num="3"></b>
                </a>
                <a class="i-4" href="#">
                    <b data-num="4"></b>
                </a>
                <a class="i-5" href="#">
                    <b data-num="5"></b>
                </a>
                <a class="i-6" href="#">
                    <b data-num="6"></b>
                </a>
                <a class="i-7" href="#">
                    <b data-num="7"></b>
                </a>
                <a class="i-8" href="#">
                    <b data-num="8"></b>
                </a>
            </div>
        </div>
    </div>
</script>

<script id="dytemp-loginbox-shadow" type="douyu/template">
    <div class="loginbox-shadow hide" id="loginbox-shadow"></div>
</script>
        <link rel="stylesheet" href="https://shark.douyucdn.cn/app/douyu/third/art-dialog-dy/skins/blue.css?4.1.7"><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/app/douyu/third/art-dialog-dy/jquery.artDialog.js?skin=blue"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/app/douyu/third/art-dialog-dy/plugins/iframeTools.js?nv=v6.887"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/app/douyu/js/page/lives/app-all.js?nv=v6.887"></script><script type="text/javascript" charset="utf-8" src="https://shark.douyucdn.cn/stream/dist/dys-douyutv.js?nv=v6.887"></script>

<svg version="1.1" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:-1000px;top:-1000px;"><filter id="grayscale312797"><feColorMatrix type="matrix" values="0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0"></feColorMatrix></filter></svg><div style="display: none; position: fixed; left: 0px; top: 0px; width: 100%; height: 100%; cursor: move; opacity: 0; background: rgb(255, 255, 255);"></div><div id="resizeListStyle" style="display: none"><style type="text/css">#live-list-content li img{height:317px;}#live-new-show-content-box li img, #live-list-content.recomended li img{height:178.3125px;}</style></div><iframe id="op-speedtest" height="0" scrolling="no" width="0" frameborder="0" style="border:none; display: none;" src="//webspeed.douyu.com/seeNet/run_test"></iframe></body></html>
"""
ret = re.findall(r'https://.*?\.jpg', d)
print(ret)
# print(len(ret))

ret1 = re.findall(r'\w*\.jpg', d)
print(ret1)

for i in range(len(ret)):
    print(i)
    request.urlretrieve(ret[i], localDir + ret1[i] )

