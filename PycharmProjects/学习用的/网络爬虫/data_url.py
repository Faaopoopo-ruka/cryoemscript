#Author：Alex.Zhang
from bs4 import BeautifulSoup
import requests
html='''

    
<!DOCTYPE html>
<html lang="zh-CN" dir="ltr" class="Mrphs-html">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Head material from Tool in PDA mode (will include title and headscripts) -->
    
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    
    <link href="/library/skin/tool_base.css?version=5c5a648" type="text/css" rel="stylesheet" media="screen, tty, tv, handheld, projection" />
<link href="/library/skin/morpheus-default/tool.css?version=5c5a648" type="text/css" rel="stylesheet" media="screen, tty, tv, handheld, projection" />
<link href="/library/skin/morpheus-default/print.css?version=5c5a648" type="text/css" rel="stylesheet" media="print" />
<script type="text/javascript" src="/library/js/headscripts.js?version=5c5a648"></script>
<script type="text/javascript">var sakai = sakai || {}; sakai.editor = sakai.editor || {}; sakai.editor.editors = sakai.editor.editors || {}; sakai.editor.editors.ckeditor = sakai.editor.editors.ckeditor || {}; sakai.locale = sakai.locale || {};
sakai.locale.userCountry = 'CN';
sakai.locale.userLanguage = 'zh';
sakai.locale.userLocale = 'zh_CN';
sakai.editor.collectionId = '/group/165118/';
sakai.editor.enableResourceSearch = false;
sakai.editor.siteToolSkin = '/library/skin/morpheus-default/tool.css';
sakai.editor.sitePrintSkin = '/library/skin/morpheus-default/print.css';
sakai.editor.editors.ckeditor.browser = 'elfinder';
</script>
<script type="text/javascript">var CKEDITOR_BASEPATH='/library/webjars/ckeditor/4.5.7/full/';
</script>
<script type="text/javascript" src="/library/webjars/ckeditor/4.5.7/full/ckeditor.js?version=5c5a648"></script>
<script type="text/javascript" src="/library/editor/ckeditor.launch.js?version=5c5a648"></script>
	
    
    	            
    
  
    <!-- End of Head material from Tool -->
 <title>Course : &#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395; : &#36164;&#28304;</title>
        <!--[if (lt IE 9)]>
  <link href="/library/skin/morpheus-default/tool-ie.css?version=5c5a648" rel="stylesheet">
<![endif]-->
<link href="/library/skin/morpheus-default/tool.css?version=5c5a648" rel="stylesheet" media="screen, tty, tv, handheld, projection">
<link href="/library/skin/morpheus-default/print.css?version=5c5a648" rel="stylesheet" media="print">        
        <link href="/library/webjars/jquery-ui/1.11.3/jquery-ui.min.css?version=5c5a648" rel="stylesheet" />  
        <link href="/library/js/jquery/cluetip/1.2.10/css/jquery.cluetip.css?version=5c5a648" rel="stylesheet">
        <link href="/library/js/jquery/qtip/jquery.qtip-latest.min.css?version=5c5a648" rel="stylesheet">
        <link href="/library/webjars/pnotify/2.1.0/pnotify.core.min.css?version=5c5a648" rel="stylesheet">
        <script src="/library/skin/morpheus-default/js/lib/modernizr.js?version=5c5a648"></script>

        <script>                                     var portal = {
                "chat": {
                    "enabled": true,
                    "pollInterval": 5000,
            "video" : {
            "enabled": true
            }
                },
                "loggedIn": true,
                "portalPath": "http://course.ucas.ac.cn/portal",
                "loggedOutUrl": "http://sep.ucas.ac.cn",
                "siteId": "165118",
                "siteTitle": "&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;",
                "shortDescription" : "",
                "locale": "zh-CN",
                "user": {
                    "id": "d0eebdb3-982c-4b04-970d-e35130cd629c",
                    "eid": "201928011215037"
                },
                "timeoutDialog" : {
                "enabled": true,
                "seconds": 600
                },
                "toggle" : {
                    "allowauto": false,
                    "tools": false,
                    "sitenav": false // This is not allowed in morpheus
                },
                "pageScriptPath" : "/library/js/",
                "portalCDNQuery" : "?version=5c5a648"
            };
        </script>
        
        <!-- inlined tool header contribution -->
                        	        		
        	                        <!-- end inlined tool header contribution -->
    </head>

    <body  class="Mrphs-portalBody course"  class="course">

        <noscript>
            <span id="portal_js_warn" class="Mrphs-noJs js-warn-no-js">Sakai需要JavaScript来提供更好的效果，请在您的浏览器中启用JavaScript</span>
        </noscript>
        
                 
        <div  class="Mrphs-portalWrapper">

                        <nav id="skipNav" class="Mrphs-skipNav">
    <ul role="menu" class="Mrphs-skipNav__menu">

                 <li role="menuitem" class="Mrphs-skipNav__menuitem Mrphs-skipNav__menuitem--content">
            <a href="#tocontent" class="Mrphs-skipNav__link" title="跳转到内容" accesskey="c">
                跳转到内容
                <span class="accesibility_key">[c]</span>
            </a>
        </li>
        <li role="menuitem" class="Mrphs-skipNav__menuitem Mrphs-skipNav__menuitem--tools">
            <a href="#totoolmenu" class="Mrphs-skipNav__link js-toggle-tools-nav" title="跳转到工具列表" accesskey="l">
                <i class="fa fa-cubes tools-icon"></i>
                工具
                <span class="accesibility_key">[l]</span>
            </a>
        </li>
        <li role="menuitem" class="Mrphs-skipNav__menuitem Mrphs-skipNav__menuitem--worksite">
            <a href="#sitetabs" id="more-sites-menu" class="Mrphs-skipNav__link js-toggle-sites-nav" title="跳转到工作站点列表" accesskey="w">
                <i class="fa fa-th all-sites-icon"></i> 我的课程
                <span class="accesibility_key">[w]</span>
            </a>
        </li>
    </ul>
</nav>

            <div  class="Mrphs-mainHeader is-maximized" >

                                <div class="Mrphs-topHeader">
                    
<header role="banner" class="Mrphs-headerLogo">
    <span class="Mrphs-headerLogo--institution"></span>
    <span class="Mrphs-headerLogo--banner"></span>
</header>                                                                    
    
    
         
         
 

         

         

         

         

         

         

         

         

         

         

         

         
 
<!-- START VM includeTabs.vm -->
    <div id="Mrphs-sites-nav" class="siteNavWrap course Mrphs-container Mrphs-container--navs">

        <nav id="linkNav" role="navigation" aria-labelledby="sitetabs" class="Mrphs-sitesNav" data-max-tools-int="10" data-max-tools-anchor="查看所有…">
    <h1 class="skip" tabindex="-1" id="sitetabs">工作站点从此处开始</h1>
    <div id="show-all-sites" tabindex="-1"><i class="fa fa-angle-double-left"></i><span>-其他站点-</span></div>
    <div id="topnav_container">
        <ul class="Mrphs-sitesNav__menu" id="topnav" role="menubar" aria-label="工作站点从此处开始">

            
        		                     <li class="Mrphs-sitesNav__menuitem Mrphs-sitesNav__menuitem--myworkspace ">
                        <a class="link-container" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037" title="我的工作空间" role="menuitem">
                            <i class="fa fa-home"></i>
                            <span class="Mrphs-sitesNav__menuitem--myworkspace-label">我的工作空间</span>
                            <span class="Mrphs-sitesNav__drop" tabindex="-1" data-site-id="~d0eebdb3-982c-4b04-970d-e35130cd629c"></span>
                        </a>
                    </li>           
                 
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                                    <li class="Mrphs-sitesNav__menuitem  is-selected ">
                        <a class="link-container" href="http://course.ucas.ac.cn/portal/site/165118" title="&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;" role="menuitem" aria-haspopup="true">
                            <span>&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;</span>
                        </a>
                        <a class="Mrphs-sitesNav__dropdown" href="#" data-site-id="165118" role="separator"></a>
                    </li>

                 
            
        		  
                                 
            
        		  
                                 
            
        		  
                                 
                     </ul>
    </div>

</nav> <!-- /Mrphs-sitesNav -->

    </div> <!-- /end of div.tabsCssClass -->
    
<!-- END VM includeTabs.vm -->

                                         
<nav id="mastLogin" class="Mrphs-loginNav">

    
        		<div class="Mrphs-sitesNav__menuitem view-all-sites-btn2">
            <a href="/library/doc/guide.pdf" target="_blank" title="课程网站快速指南" role="menuitem" aria-haspopup="true">
                <i class="fa fa-question-circle all-sites-icon"></i> <span class="all-sites-label">课程网站快速指南</span>
            </a>
        </div>
                    <div class="Mrphs-sitesNav__menuitem view-all-sites-btn">
                <a href="javascript:void(0);" title="查看所有课程" role="menuitem" aria-haspopup="true">
                    <i class="fa fa-th all-sites-icon"></i> <span class="all-sites-label">我的课程</span>
                </a>
            </div>
        
        <ul id="loginLinks" class="Mrphs-userNav">

                
                    
                        <li class="Mrphs-userNav__popup js-toggle-user-nav" aria-haspopup="true">

                                
                                    
                                        <div id="loginUser" role="menuitem" class="has-avatar Mrphs-userNav__submenuitem--userlink ">
                                            <a href="javascript:void(0);" class="Mrphs-userNav__drop-btn Mrphs-userNav__submenuitem--profilepicture" style="background-image:url(/direct/profile/d0eebdb3-982c-4b04-970d-e35130cd629c/image/thumb)" tabindex="-1"></a>
                                            <a href="javascript:void(0);" class="Mrphs-userNav__drop-btn Mrphs-userNav__submenuitem--username">&#24352;&#28009;&#26976;</a>
                                        </div>

                                     
                                 
                            <ul class="Mrphs-userNav__subnav is-hidden" role="menu">

                                <li class="Mrphs-userNav__submenuitem Mrphs-userData">
                                    <div class="Mrphs-userNav__submenuitem--profile-and-image">
                                                                                    <div class="has-avatar">
                                                <a class="Mrphs-userNav__submenuitem--profilelink" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/tool-reset/33652c55-8290-4c85-8de5-041578ad7a83">
                                                    <span class="Mrphs-userNav__submenuitem--profilepicture" style="background-image:url(/direct/profile/d0eebdb3-982c-4b04-970d-e35130cd629c/image/thumb)" tabindex="-1"></span>
                                                </a>
                                            </div>
                                            <div class="Mrphs-userNav__submenuitem--profile">
                                                <a role="menuitem" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/tool-reset/33652c55-8290-4c85-8de5-041578ad7a83">
                                                    <span>个人资料</span>
                                                </a>
                                            </div>
                                                                            </div>
                                    <div class="Mrphs-userNav__submenuitem--fullname-and-id">
                                        <div class="Mrphs-userNav__submenuitem--fullname">
                                            &#24352;&#28009;&#26976;
                                        </div>
                                        <div class="Mrphs-userNav__submenuitem--displayid">
                                            201928011215037
                                        </div>
                                    </div>
                                </li>
                                
                                    
                                        <li class="Mrphs-userNav__submenuitem Mrphs-userNav__submenuitem-indented">
                                            <a role="menuitem" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/page/8173875f-44d4-4787-a342-50bafa777c1e" class="Mrphs-userNav__submenuitem--prefs">
                                                <span>用户偏好</span>
                                            </a>
                                        </li>

                                     
                                    
                                        
                                            <li class="Mrphs-userNav__submenuitem Mrphs-userNav__submenuitem-indented">
                                                <a id="addNewSiteLink" role="menuitem" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/tool-reset/ff2658b2-e9cf-41a2-a415-9998ad97e03e?panel=Shortcut&amp;sakai_action=doNew_site" class="Mrphs-userNav__submenuitem--newsite">
                                            <span>+ 添加新课程</span>
                                                </a>
                                            </li>

                                         
                                     
                                    
                                        <li class="Mrphs-userNav__submenuitem Mrphs-userNav__submenuitem-indented">
                                            <a id="tutorialLink" role="menuitem" href="#" onclick="startTutorial({});" class="Mrphs-userNav__submenuitem--tutorial">
                                                <span>教程</span>
                                            </a>
                                        </li>

                                     
                             
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                        
                     
                         
                            <li class="Mrphs-userNav__logout Mrphs-userNav__submenuitem-indented">
                                <div id="loginLinksImage" class="Mrphs-loginUser" role="menu" tabindex="999">

    
        <p role="menuitem" class="Mrphs-loginUser__menuitem">
            <a href="http://course.ucas.ac.cn/portal/logout" title="注销" target="_top" id="loginLink1" class="Mrphs-loginUser__message" data-warning="">
                <i class="login-Icon"></i>
                <span class="Mrphs-login-Message">注销</span>
            </a>
        </p>

     
     
</div>                            </li>

                        </ul>

            </li>

        </ul> <!-- end of nav#loginLinks-->

             
</nav>
                </div>
                
            </div>

                <div id="maxToolsText" style="display: none">查看所有…</div>
    <div id="maxToolsInt" style="display: none">10</div>
    <div id="refreshNotificationText" style="display: none"><a href="javascript:location.reload()">重新载入</a> 来查看更新的偏好站点</div>
    <div id="addToFavoritesText" style="display: none">加入偏好站点</div>
    <div id="removeFromFavoritesText" style="display: none">从偏好站点移除</div>

    <div id="selectSiteModal" class="outscreen">

        <ul id="otherSitesMenu">
            
                <li><a id="allSites" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/tool-reset/ff2658b2-e9cf-41a2-a415-9998ad97e03e"><span>查看所有课程</span></a></li>

                
                    <li><a id="newSite" href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/tool-reset/ff2658b2-e9cf-41a2-a415-9998ad97e03e?panel=Shortcut&amp;sakai_action=doNew_site&amp"><span>+ 添加新课程</span></a></li>

                 
             
            
                <li><a href="http://course.ucas.ac.cn/portal/site/%7E201928011215037/page/8173875f-44d4-4787-a342-50bafa777c1e"><span>用户偏好</span></a></li>

             
            <li class="otherSitesMenuClose"><a href="javascript:void(0);"><i class="fa fa-times"></i></a></li>
        </ul>

        <div id="selectSite">
            <!-- View all sites, add new site, preferences -->
            <ul class="tab-bar">
                <li class="tab-btn active" data-tab-target="otherSitesCategorWrap"><h2 class="favorites-tab-label">我的课程</h2></li>
                <li class="organizeFavorites tab-btn" data-tab-target="organizeFavorites">
                    <h2 class="favorites-tab-label"><span class="favorites-desktop">管理偏好课程</span><span class="favorites-mobile">偏好站点</span> <span class="favoriteCount"></span></h2></li>
            </ul>

            <div class="tab-pane">
                <div class="tab-box" id="otherSitesCategorWrap">

                    <div id="otherSiteSearch">
                        <label class="sr-only" for="txtSearch">在课程列表中搜索"</label>
                        <input type="text" id="txtSearch" name="txtSearch" maxlength="50" placeholder=" 在课程列表中搜索">
                        <a id="otherSiteSearchClear" class="other-site-search-clear" href="javascript:void(0);"></a>
                    </div>
                    <div id="noSearchResults" class="is-hidden">没有找到任何结果</div>


                    
                    <div class="moresites-left-col">
                                                                                                                                        <div class="fav-sites-term">
                                                                            <h3 class="favorites-term-header">2019—2020学年(秋)第一学期</h3>
                                    
                                    <ul class="otherSitesCategorList favoriteSiteList">
                                                                                                            <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165683" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165683" title="&#20013;&#22269;&#29305;&#33394;&#31038;&#20250;&#20027;&#20041;&#29702;&#35770;&#19982;&#23454;&#36341;&#30740;&#31350;&#65288;&#19996;&#21306;&#65289;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#20013;&#22269;&#29305;&#33394;&#31038;&#20250;&#20027;&#20041;&#29702;&#35770;&#19982;&#23454;&#36341;&#30740;&#31350;&#65288;&#19996;&#21306;&#65289;19 ...</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165683" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="167605" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/167605" title="&#23398;&#26415;&#36947;&#24503;&#19982;&#23398;&#26415;&#20889;&#20316;&#35268;&#33539;-&#20998;&#35770;-1&#29677;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#23398;&#26415;&#36947;&#24503;&#19982;&#23398;&#26415;&#20889;&#20316;&#35268;&#33539;-&#20998;&#35770;-1&#29677;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="167605" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="166583" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/166583" title="&#23398;&#26415;&#36947;&#24503;&#19982;&#23398;&#26415;&#20889;&#20316;&#35268;&#33539;-&#36890;&#35770;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#23398;&#26415;&#36947;&#24503;&#19982;&#23398;&#26415;&#20889;&#20316;&#35268;&#33539;-&#36890;&#35770;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="166583" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165051" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165051" title="&#23454;&#29992;&#26368;&#20248;&#21270;&#31639;&#27861;&#21450;&#20854;&#24212;&#29992;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#23454;&#29992;&#26368;&#20248;&#21270;&#31639;&#27861;&#21450;&#20854;&#24212;&#29992;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165051" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="166732" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/166732" title="&#29983;&#29289;&#20449;&#24687;&#23398;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#29983;&#29289;&#20449;&#24687;&#23398;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="166732" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165131" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165131" title="&#29983;&#29289;&#22823;&#20998;&#23376;&#30340;&#30005;&#38236;&#19977;&#32500;&#32467;&#26500;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#29983;&#29289;&#22823;&#20998;&#23376;&#30340;&#30005;&#38236;&#19977;&#32500;&#32467;&#26500;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165131" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165463" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165463" title="&#31185;&#30740;&#20262;&#29702;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#31185;&#30740;&#20262;&#29702;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165463" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165108" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165108" title="&#31185;&#30740;&#35770;&#25991;&#20889;&#20316;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#31185;&#30740;&#35770;&#25991;&#20889;&#20316;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165108" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry is-selected  ">
                                                        	<a class="site-favorite-btn" data-site-id="165118" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165118" title="&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165118" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="167752" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/167752" title="&#33521;&#35821;A&#20998;&#32423;&#32771;&#35797;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#33521;&#35821;A&#20998;&#32423;&#32771;&#35797;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="167752" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                                <li class="fav-sites-entry  ">
                                                        	<a class="site-favorite-btn" data-site-id="165121" href="javascript:void(0);"></a>
                            							
                            <div class="fav-title ">
                            	<a href="http://course.ucas.ac.cn/portal/site/165121" title="&#34920;&#35266;&#36951;&#20256;&#23398;19-20&#31179;&#23395;">
                                                                            <span class="fullTitle">&#34920;&#35266;&#36951;&#20256;&#23398;19-20&#31179;&#23395;</span>
                                                                    </a>
                            </div>
                            <a href="#" id="165121" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                </ul>
                                </div>
                                                                        </div>

                    <div class="moresites-right-col">
                                                                                    <div class="fav-sites-term">
                                                                            <h3 class="favorites-term-header">其他站点</h3>

                                        <ul class="otherSitesCategorList favoriteSiteList">
                                            <!-- anchor "my workspace" to the top of the list -->
                                                                                                                                                                        <li class="fav-sites-entry  my-workspace ">
                            							
                            <div class="fav-title  fav-title-myworkspace ">
                            	<a href="http://course.ucas.ac.cn/portal/site/%7E201928011215037" title="My Workspace">
                                                                            <i class="fa fa-home"></i><span class="fullTitle">我的工作空间</span>
                                                                    </a>
                            </div>
                            <a href="#" id="~d0eebdb3-982c-4b04-970d-e35130cd629c" class="toolMenus"><i class="fa fa-chevron-down"></i></a>
                        </li>
                                                                                                                
                                                                                                                                                                                </ul>
                                                                    </div>
                                                                                                                            </div>

                </div><!--  end of #otherSitesCategorWrap -->

                <div style="display: none" class="tab-box" id="organizeFavorites">
                    <h2 class="heading">管理偏好课程</h2>

                    <ul id="organizeFavoritesList" class="organizeFavoritesList favoriteSiteList">
                    </ul>

                    <!-- Items are put here when unfavorited from the "organize" screen -->
                    <ul id="organizeFavoritesPurgatoryList" class="favoriteSiteList">
                    </ul>
                </div>
            </div>
        </div>
    </div>

            <!-- START VM includePageWithNav.vm -->

    <nav class="Mrphs-siteHierarchy">

                 
                                            <span class="Mrphs-hierarchy--siteName" title="&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395;">
                    <a href="http://course.ucas.ac.cn/portal/site/165118/page-reset/d39cc557-0a88-44c6-bb1c-54f33deb22f4">结构生物学技术19-20秋季</a>
                </span>
                <span class="Mrphs-hierarchy--siteNameSeparator Mrphs-hierarchy--separator"><i class="fa fa-lg fa-angle-right"></i></span>
                                                                                                                                                                                                                                                                                                            
        
                                                                                            <a href="http://course.ucas.ac.cn/portal/site/165118/tool-reset/a23d6b3e-4714-4479-82ae-8642ecf0d1f4" title="重置" class="Mrphs-hierarchy-item Mrphs-hierarchy--toolName">
                <span class="Mrphs-breadcrumb--reset-icon fa fa-share" aria-hidden="true"></span>
                <span class="Mrphs-breadcrumb--icon icon-sakai--sakai-resources "></span>
                <span>&#36164;&#28304;</span>
            </a>
                                                                                                                                                                                                                                                    </nav>

    <div id="pageBody">
    
    
        <!-- START VM includePageNav.vm -->

<div id="toolMenuWrap" class="Mrphs-container Mrphs-container--nav-tools" >

     
    <h1 class="skip" tabindex="-1" id="totoolmenu">工具从此处开始</h1>
    <!--Added this check in to make sure that we just don't have an empty img element in the page. -->
	
	<div id="toolSubsitesContainer">
		<nav id="toolMenu" role="navigation" aria-label="工具从此处开始" class="Mrphs-toolsNav__menu">
			<ul>
				<li class="Mrphs-toolsNav__menuitem Mrphs-collapseTools js-toggle-nav">
					<i class="fa fa-lg fa-angle-double-left"></i>
				</li>
				 	
				
												
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/page/d39cc557-0a88-44c6-bb1c-54f33deb22f4" title="&#20027;&#39029; - 显示最近的通知，有新通知时更新 | 在我的工作空间显示日程汇总 | 教师信息 | 最新资源">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-synoptic-announcement "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#20027;&#39029;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/a01677f3-68a7-4265-883b-3a55a91ffb18" title="&#35838;&#31243;&#22823;&#32434; - 站点/课程概要或要求">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-syllabus "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#35838;&#31243;&#22823;&#32434;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/e44b2ead-7c9e-46e7-aa9f-edb7c65ea3d9" title="&#35838;&#31243;&#30446;&#24405; - 课程目录">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-coursecontents "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#35838;&#31243;&#30446;&#24405;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
						<li class="Mrphs-toolsNav__menuitem is-current">
							<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool-reset/a23d6b3e-4714-4479-82ae-8642ecf0d1f4" title="&#36164;&#28304;" role="presentation">
								<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-resources  icon-active"></span>
								<span class="Mrphs-toolsNav__menuitem--title">&#36164;&#28304;</span>
							</a>
						</li>
	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/9527ed04-e0d7-416a-88c6-e3f5bb078d31" title="&#35838;&#31243;&#35270;&#39057; - 课程视频">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-kcsp "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#35838;&#31243;&#35270;&#39057;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/212a7fe6-2b2d-402b-9bbc-ee160b11c811" title="&#20316;&#19994; - 在线发布、提交和批改作业">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-assignment-grades "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#20316;&#19994;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/9888d364-2a24-4b09-968c-f582c9d5961c" title="&#32451;&#20064;&#19982;&#27979;&#39564; - 进行在线练习和考试">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-samigo "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#32451;&#20064;&#19982;&#27979;&#39564;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/fbb5874c-623b-45f4-bc8e-37c4b241246c" title="&#31449;&#28857;&#20449;&#24687; - 显示站点信息和站点用户，对站点进行管理">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-siteinfo "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#31449;&#28857;&#20449;&#24687;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/2bb05e3f-b2d6-4cad-b97d-f4bad453d6d6" title="&#25104;&#32489;&#20876; - 保存和计算测验工具中的成绩，或手工输入成绩">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-gradebook-tool "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#25104;&#32489;&#20876;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/28f618c9-c2e2-45b4-9cc5-8e4d4e1341d7" title="&#26085;&#31243; - 发布和查看事件，截止日期等">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-schedule "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#26085;&#31243;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/75e95864-c42c-4fcf-a305-5d9cab71a5b7" title="&#36890;&#30693; - 通知公告工具，发布和站点相关的消息">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-announcements "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#36890;&#30693;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/23032541-a25a-4f14-b947-7a2ead2f2f73" title="&#32842;&#22825;&#23460; - 基于文本的实时聊天工具">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-chat "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#32842;&#22825;&#23460;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/484e8ef9-ce5a-4789-bb8a-57dcffbafa5d" title="&#35752;&#35770;&#21306; - 在站点内进行讨论，可与首页集成">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-forums "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#35752;&#35770;&#21306;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/962b965b-aa2d-4588-aa9f-ce9f70ea0b1f" title="&#30005;&#23376;&#37038;&#20214; - 发送邮件给指定的站点成员">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-mailtool "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#30005;&#23376;&#37038;&#20214;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
													
							
								
								<li>
									<a class="Mrphs-toolsNav__menuitem--link " href="http://course.ucas.ac.cn/portal/site/165118/tool/6dd2607a-5332-4464-b33d-9c152909707f" title="&#31449;&#28857;&#35780;&#20272; - 站点评估">
										<span class="Mrphs-toolsNav__menuitem--icon icon-sakai--sakai-courseeval "></span>
										<span class="Mrphs-toolsNav__menuitem--title">&#31449;&#28857;&#35780;&#20272;</span>
									</a>
								</li>
	
							 	
						 	
					 			 	
				 	
			
		 	
				 	
					
					<li class="Mrphs-toolsNav__menuitem--help">
						<a class="Mrphs-toolsNav__menuitem--link" accesskey="6" href="http://course.ucas.ac.cn/portal/help/main" target="_blank" onclick="openWindow('http://course.ucas.ac.cn/portal/help/main', 'Help', 'resizable=yes,toolbar=no,scrollbars=yes,menubar=yes,width=1024,height=768'); return false" title="帮助">
							<span  class="Mrphs-toolsNav__menuitem--icon icon-sakai--help"> </span>
							<span class="Mrphs-toolsNav__menuitem--title">帮助</span>
							<span class="skip">在新窗口打开</span>
						</a>
					</li>
	
				 	
				 	
			</ul>
		</nav>
	
		 	</div>
</div>

<!-- END VM includePageNav.vm -->

     
    <div class="Mrphs-pagebody">
       
        

    

 
<!-- START VM includePageBody.vm -->

<h1 class="skip" tabindex="-1" id="tocontent">内容从这里开始</h1>

        
    <main id="content" class="Mrphs-mainContent " role="main">

        
 
        <div id="col1" class="Mrphs-pageColumns Mrphs-pageColumns--single">

            
                
                                    
                    <!-- start Tool Container -->
                    
                    
                    <div class="Mrphs-container Mrphs-sakai-resources">
                    
                    <!-- start Tool Header -->

                    
                        

                            <nav class="Mrphs-toolTitleNav Mrphs-container--toolTitleNav">

                                
                                    
                                        <h2 class="Mrphs-toolTitleNav__title">
                                            <a href="http://course.ucas.ac.cn/portal/site/165118/tool-reset/a23d6b3e-4714-4479-82ae-8642ecf0d1f4" title="重置: &#36164;&#28304;">
                                                <span class="Mrphs-toolTitleNav__link Mrphs-toolTitleNav__link--reset"></span>
                                                <span class="Mrphs-toolTitleNav__text">&#36164;&#28304;</span>
                                            </a>
					    <span class="Mrphs-toolTitleNav__addLeft"></span>
                                        </h2>

                                     
                                 
                                <div class="Mrphs-toolTitleNav__button_container">
                                
                                 
				                <span class="Mrphs-toolTitleNav__addRight"></span>
                                
                                    <a class="Mrphs-toolTitleNav__link Mrphs-toolTitleNav__link--directurl" href="#Maina23d6b3ex4714x4479x82aex8642ecf0d1f4_directurl" rel="#Maina23d6b3ex4714x4479x82aex8642ecf0d1f4_directurl" title="工具链接">
                                        <span class="Mrphs-itemTitle">链接</span>
                                    </a>
                                    <div id="Maina23d6b3ex4714x4479x82aex8642ecf0d1f4_directurl" class="Mrphs-directUrl Mrphs-directUrl__dropDown">
                                        <i class="fa fa-times dropDown_close"></i>
                                        
                                            <input type="checkbox" id="directToolUrl-1" onclick="toggleShortUrlOutput('http://course.ucas.ac.cn/portal/directtool/a23d6b3e-4714-4479-82ae-8642ecf0d1f4/', this, 'Maina23d6b3ex4714x4479x82aex8642ecf0d1f4_urlholder');" class="Mrphs-directUrl__checkbox"><label for="directToolUrl-1">短链接</label>

                                         
                                        <textarea class="Mrphs-directUrl__textarea Maina23d6b3ex4714x4479x82aex8642ecf0d1f4_urlholder" >http://course.ucas.ac.cn/portal/directtool/a23d6b3e-4714-4479-82ae-8642ecf0d1f4/</textarea>
                                    </div>

                                 
                                
                                    
                                        <a class="Mrphs-toolTitleNav__link Mrphs-toolTitleNav__link--help-popup" href="http://course.ucas.ac.cn/portal/help/main?help=sakai.resources" title="&#36164;&#28304;的帮助" target="_blank" onclick="openWindow('http://course.ucas.ac.cn/portal/help/main?help=sakai.resources', 'Help', 'resizable=yes,toolbar=no,scrollbars=yes,menubar=yes,width=1024,height=768'); return false">
                                            <span class="Mrphs-itemTitle">帮助</span>
                                            <span class="skip">在新窗口打开</span>
                                        </a>

                                     
                                 
                                </div>

                            </nav> 
                         
                     
                    <!-- END Tool Header -->

                    <!-- START Tool Body -->

                    
                        <!-- Buffered Body Tool Content -->
                        
<!-- sakai_resources_list.vm, use with org.sakaiproject.content.tool.ResourcesAction.java -->
<!-- this is the new list template, which uses the resources type registry -->
<script type="text/javascript">includeLatestJQuery('content');</script>

<!-- // -->
</script>

<style>
  .table td, .table th {
    vertical-align: middle !important;
    text-align:left !important;
  }
</style>

	<script type="text/javascript" src="/sakai-content-tool/js/content.js?version=5c5a648"></script>
<!-- // -->
</script>


<script type="text/javascript">
    var jsLang = {
        item:'项',
        items:'项',
        error:'对不起 - 不能获取信息。'
    }    
</script>

	<script type="text/javascript" src="/sakai-content-tool/js/jstree/dist/jstree.min.js?version=5c5a648"></script>
    <link type="text/css" href="/sakai-content-tool/js/jstree/dist/themes/default/style.min.css?version=5c5a648" rel="stylesheet" />
<div id="dialog-copyright"></div>
<div class="portletBody specialLink">
			<ul class="navIntraTool actionToolBar">
            			<li class="firstToolBarItem"><span class="current">站点资源</span></li>
            																													</ul>
		</ul>
						<form name="showForm" id="showForm" action="http://course.ucas.ac.cn/portal/site/165118/tool/a23d6b3e-4714-4479-82ae-8642ecf0d1f4" method="post">
						<input type="hidden" name="source" id="source" value="0" />
		<input type="hidden" name="collectionId" id="collectionId" value="/group/165118/" />
		<input type="hidden" name="navRoot" id="navRoot" value="" />
		<input type="hidden" name="criteria" id="criteria" value="title" />
		<input type="hidden" name="sakai_action" id="sakai_action" value="" />
		<input type="hidden" name="rt_action" id="rt_action" value="" />
		<input type="hidden" name="selectedItemId" id="selectedItemId" value="" />
		    <br>
    <ol class="breadcrumb">
              <li class="dropdown keep-open">
          <a id="navigate" data-toggle="dropdown" href="">
            所有站点文件 <span class="caret"></span>
          </a>
          <div id="navigatePanel" class="dropdown-menu" role="menu">
            <div class="navigatePanelControls">
              <span class="expand_collapse">
                <button id="navigatePanelInnerCollapse" style="display:none" class="btn btn-link btn-xs" title="折叠全部">
                  <span class="glyphicon glyphicon-chevron-up"></span>
                  <span class="sr-only">折叠全部</span>
                </button> 
              </span>
              <button id="navigatePanelInnerExpand" class="btn btn-link btn-xs" onclick="$('#navigatePanelInner').jstree('open_all')" title="展开所有"><span class="glyphicon glyphicon-chevron-down"></span><span class="sr-only">展开所有</span></button></span>
              <label for="navigatePanelSearch" class="sr-only">搜索</label>
              <input placeholder="搜索" type="text" id="navigatePanelSearch"/>
              <p class="close">&times;</p>
            </div>
            <div id="navigatePanelInner">
              <div id="spinner" style="display:none"><i class="fa fa-circle-o-notch fa-2x fa-spin" ></i></div>
            </div>
          </div>
        </li>
                              <li class="active">
            &#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395; &#36164;&#28304;
          </li>
                    <li><a href="/library/doc/resource_upload_guide.pdf" target="_blank">如何上传讲义课件</a></li>
    </ol>

  
    <div class="container-fluid">
      <div class="row">
    		    				<div class="col-lg-6 col-md-8 col-sm-8 col-xs-12 btn-group btn-group-sm" role="group" style="padding-left:0;">
    					    							    								<button style="margin:0" class="btn btn-default" id="copy-button"
    									onclick="document.getElementById('sakai_action').value='doMultiItemDispatch';document.getElementById('rt_action').value='copy';document.getElementById('showForm').submit();"
    									disabled="disabled" >复制
                                    </button>
    							
                                                                                                                                                                                                                                      
    					    				</div>
    		        <div class="col-xs-12 col-lg-6 col-md-4 col-sm-4 col-xs-4 btn-group btn-group-sm form-inline" style="text-align: right;padding-right:0">
                                      <span class="hidden-sm hidden-xs pull-right">
                <button style="margin:0" type="button" class="btn btn-default btn-sm resources-dropdown colPicker" aria-expanded="false" data-toggle="dropdown">
                  显示列
                  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" id="columnTog">
                  <li class="dropdown-button">
                      <span class="close-button"></span>
                  </li>
                  <li class="dropdown-header"><span>要显示的列</span></li>
                  <li class="dropdown-header"><span id="accessTog"><input type="checkbox" id="accessCol" checked="checked" /><label for="accessCol">&nbsp;&nbsp;访问范围</label></span></li>
                  <li class="dropdown-header"><span id="creatorTog"><input type="checkbox" id="creatorCol" checked="checked" /><label for ="creatorCol">&nbsp;&nbsp;创建者</label></span></li>
                  <li class="dropdown-header"><span id="modifiedTog"><input type="checkbox" id="modifiedCol" checked="checked"/><label for="modifiedCol">&nbsp;&nbsp;最后修改时间</label></span></li>
                  <li class="dropdown-header"><span id="sizeTog"><input type="checkbox" id="sizeCol" checked="checked"/><label for="sizeCol">&nbsp;&nbsp;大小</label></span></li>
                  <li class="dropdown-header"><button class="btn btn-primary  btn-sm btn-block" id="saveCols">保存</button></li>
                </ul>
              </span>
                    </div>
      </div>
    </div>
    <p></p>
    <div id="userId" style="display: none;">d0eebdb3-982c-4b04-970d-e35130cd629c</div>
		    		<table style="margin:0;width:100%;display:table" class="table table-striped table-hover  resourcesList " cellspacing="0" border="0"  summary="资源列表，点击列标题可排序，其中第一列指示项目是否被移动、复制或删除，第二列是复选框，第三列是资源或文件夹链接，第四列是操作链接，第五列是修改日期，第六列是作者，第七列是资源大小。">
						<caption class="skip"  style="display:none">资源列表</caption>
			<tr class="hidden-sm hidden-xs"> 
				<th id="expansion" class="attach" scope="col">
											<a href="#" onclick="document.getElementById('sakai_action').value='doExpandall';document.getElementById('collectionId').value='/group/165118/';document.getElementById('showForm').submit();"
							title= "展开所有">
                            <span class="sr-only">展开所有</span>
                            <span class="glyphicon glyphicon-chevron-down"></span>
													</a>								 
									</th>
				<th id="checkboxes" class="attach" scope="col">
						<input type="checkbox" name="selectall" id="selectall" disabled="disabled" title="全部选择"
						onclick="toggleSelectAll(this, 'selectedMembers'); adjustShowHideCount(this)" value="" /><label for="selectall" class="skip">全部选择</label>

				</th>
				<th id="title" scope="col" style="text-align:left">
					<a href="#" onclick="document.getElementById('sakai_action').value='doSort';document.getElementById('collectionId').value='/group/165118/';document.getElementById('criteria').value='title';document.getElementById('showForm').submit();"
						title= "按标题排序">
						标题
																					<img src = "/library/image/sakai/sortascending.gif" border="0" title ="按标题升序排列" alt ="按标题升序排列" /> 
																		</a>
				</th>
				<th id="actions1" class="attach" scope="col">
									</th>
				<th id="actions2" class="actions2" scope="col">
									</th>
				<th id="access" class="access" scope="col">
					访问范围
				</th>
				<th id="creator" class="creator" scope="col">
					<a href="#" onclick="document.getElementById('sakai_action').value='doSort';document.getElementById('collectionId').value='/group/165118/';document.getElementById('criteria').value='created by';document.getElementById('showForm').submit();"
						title= "按作者排序">
						创建者
											</a>
				</th>
				<th id="modified" class="modified" scope="col">
					<a href="#" onclick="document.getElementById('sakai_action').value='doSort';document.getElementById('collectionId').value='/group/165118/';document.getElementById('criteria').value='last modified';document.getElementById('showForm').submit();"
						title= "按最近修改日期排序">
						最后修改时间
											</a>
				</th>
				<th id="size" class="size" scope="col">
					<a href="#" onclick="document.getElementById('sakai_action').value='doSort';document.getElementById('collectionId').value='/group/165118/';document.getElementById('criteria').value='size';document.getElementById('showForm').submit();"
						title= "按文件大小排序">
						大小
											</a>
				</th>
			</tr>
																		
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
											</td>
					<td style="text-indent:0em" class="specialLink title" scope="row">
					                            
              																	<span class="skip"></span>
																			<span class="nil">
										<img src="/library/image/sakai/dir_closed.gif" border= "0" alt="文件夹" hspace="0" /></span>
																		
																								    																		<a href="#"
    										onclick="document.getElementById('sakai_action').value='doNavigate';document.getElementById('collectionId').value='/group/165118/';document.getElementById('navRoot').value='';document.getElementById('showForm').submit();"
    										title= "文件夹">
                        <span class="visible-sm-inline visible-xs-inline">&#32467;&#26500;&#29983;& ...</span>
                        <span class="hidden-sm hidden-xs">&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395; &#36164;&#28304;</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;19-20&#31179;&#23395; &#36164;&#28304; 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/';document.getElementById('rt_action').value='org.sakaiproject.content.types.folder:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/';document.getElementById('rt_action').value='org.sakaiproject.content.types.folder:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
					                        <td class="access hidden-sm hidden-xs">
                        </td>
                        <td class="creator hidden-sm hidden-xs">
                        </td>
                        <td class="modified hidden-sm hidden-xs">
                        </td>
                        <td class="size hidden-sm hidden-xs">
                        </td>						

									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list2" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Biochemistry_chap04_protein_structure.pdf" /><label for="list2" class="skip">选择: Biochemistry_chap04_protein_structure.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Biochemistry_chap04_protein_structure.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Biochemistry_chap04_protein_structure.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Biochemistry_chap04_prote ...</span>
                        <span class="hidden-sm hidden-xs">Biochemistry_chap04_protein_structure.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Biochemistry_chap04_protein_structure.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Biochemistry_chap04_protein_structure.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Biochemistry_chap04_protein_structure.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:14
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							5.5 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list3" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/crystallography_ITA_dauter_2011.pdf" /><label for="list3" class="skip">选择: crystallography_ITA_dauter_2011.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/crystallography_ITA_dauter_2011.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/crystallography_ITA_dauter_2011.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">crystallography_ITA_daute ...</span>
                        <span class="hidden-sm hidden-xs">crystallography_ITA_dauter_2011.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">crystallography_ITA_dauter_2011.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/crystallography_ITA_dauter_2011.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/crystallography_ITA_dauter_2011.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							3.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list4" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf" /><label for="list4" class="skip">选择: Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Drenth_Principles%20of%20Protein%20X-Ray%20Crystallography%203rd%20ed.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Drenth_Principles%20of%20Protein%20X-Ray%20Crystallography%203rd%20ed.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Drenth_Principles of Prot ...</span>
                        <span class="hidden-sm hidden-xs">Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Drenth_Principles of Protein X-Ray Crystallography 3rd ed.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							4.3 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list5" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/forcefield.pdf" /><label for="list5" class="skip">选择: forcefield.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/forcefield.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/forcefield.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">forcefield.pdf</span>
                        <span class="hidden-sm hidden-xs">forcefield.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">forcefield.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/forcefield.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/forcefield.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							2.5 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list6" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture0_Introduction_KY.pdf" /><label for="list6" class="skip">选择: Lecture0_Introduction_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture0_Introduction_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture0_Introduction_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture0_Introduction_KY. ...</span>
                        <span class="hidden-sm hidden-xs">Lecture0_Introduction_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture0_Introduction_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture0_Introduction_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture0_Introduction_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							194.1 KB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list7" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture1_structuralbiology_KY.pdf" /><label for="list7" class="skip">选择: Lecture1_structuralbiology_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture1_structuralbiology_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture1_structuralbiology_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture1_structuralbiolog ...</span>
                        <span class="hidden-sm hidden-xs">Lecture1_structuralbiology_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture1_structuralbiology_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture1_structuralbiology_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture1_structuralbiology_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:22
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							12.4 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list8" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture2_PyMOL_KY.pdf" /><label for="list8" class="skip">选择: Lecture2_PyMOL_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture2_PyMOL_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture2_PyMOL_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture2_PyMOL_KY.pdf</span>
                        <span class="hidden-sm hidden-xs">Lecture2_PyMOL_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture2_PyMOL_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture2_PyMOL_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture2_PyMOL_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							15.3 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list9" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture3_math_KY.pdf" /><label for="list9" class="skip">选择: Lecture3_math_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture3_math_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture3_math_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture3_math_KY.pdf</span>
                        <span class="hidden-sm hidden-xs">Lecture3_math_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture3_math_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture3_math_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture3_math_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list10" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture4_crystal_KY.pdf" /><label for="list10" class="skip">选择: Lecture4_crystal_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture4_crystal_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture4_crystal_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture4_crystal_KY.pdf</span>
                        <span class="hidden-sm hidden-xs">Lecture4_crystal_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture4_crystal_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture4_crystal_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture4_crystal_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							3.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list11" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture5_diffraction_KY.pdf" /><label for="list11" class="skip">选择: Lecture5_diffraction_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture5_diffraction_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture5_diffraction_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture5_diffraction_KY.p ...</span>
                        <span class="hidden-sm hidden-xs">Lecture5_diffraction_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture5_diffraction_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture5_diffraction_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture5_diffraction_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							7.6 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list12" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Lecture6_phasing_KY.pdf" /><label for="list12" class="skip">选择: Lecture6_phasing_KY.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture6_phasing_KY.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Lecture6_phasing_KY.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Lecture6_phasing_KY.pdf</span>
                        <span class="hidden-sm hidden-xs">Lecture6_phasing_KY.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Lecture6_phasing_KY.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture6_phasing_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Lecture6_phasing_KY.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							6.7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list13" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/McRee_Practical Protein Crystallography 2nd ed.pdf" /><label for="list13" class="skip">选择: McRee_Practical Protein Crystallography 2nd ed.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/McRee_Practical%20Protein%20Crystallography%202nd%20ed.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/McRee_Practical%20Protein%20Crystallography%202nd%20ed.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">McRee_Practical Protein C ...</span>
                        <span class="hidden-sm hidden-xs">McRee_Practical Protein Crystallography 2nd ed.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">McRee_Practical Protein Crystallography 2nd ed.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/McRee_Practical Protein Crystallography 2nd ed.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/McRee_Practical Protein Crystallography 2nd ed.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							39.4 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list14" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf" /><label for="list14" class="skip">选择: Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Molecular%20Modeling%20and%20Simulation%20-%20An%20Interdisciplinary%20Guide%202ed%202010.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Molecular%20Modeling%20and%20Simulation%20-%20An%20Interdisciplinary%20Guide%202ed%202010.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Molecular Modeling and Si ...</span>
                        <span class="hidden-sm hidden-xs">Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Molecular Modeling and Simulation - An Interdisciplinary Guide 2ed 2010.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							16.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list15" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Molecular modelling - principles and applications 2001.pdf" /><label for="list15" class="skip">选择: Molecular modelling - principles and applications 2001.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Molecular%20modelling%20-%20principles%20and%20applications%202001.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Molecular%20modelling%20-%20principles%20and%20applications%202001.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Molecular modelling - pri ...</span>
                        <span class="hidden-sm hidden-xs">Molecular modelling - principles and applications 2001.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Molecular modelling - principles and applications 2001.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Molecular modelling - principles and applications 2001.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Molecular modelling - principles and applications 2001.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							43.4 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list16" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/par_all36_prot.prm" /><label for="list16" class="skip">选择: par_all36_prot.prm</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/par_all36_prot.prm" target="_blank">
																			<img src="/library/image/sakai/text.gif" border= "0" alt="文本" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/par_all36_prot.prm" target="_blank" title="文本">
                        <span class="visible-sm-inline visible-xs-inline">par_all36_prot.prm</span>
                        <span class="hidden-sm hidden-xs">par_all36_prot.prm</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">par_all36_prot.prm 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/par_all36_prot.prm';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/par_all36_prot.prm';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							180.9 KB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list17" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Protein NMR Techniques.pdf" /><label for="list17" class="skip">选择: Protein NMR Techniques.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Protein%20NMR%20Techniques.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Protein%20NMR%20Techniques.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Protein NMR Techniques.pd ...</span>
                        <span class="hidden-sm hidden-xs">Protein NMR Techniques.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Protein NMR Techniques.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Protein NMR Techniques.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Protein NMR Techniques.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							10.3 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list18" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/PyMOLmaterials_new.rar" /><label for="list18" class="skip">选择: PyMOLmaterials_new.rar</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/PyMOLmaterials_new.rar" target="_self">
																			<img src="/library/image//sakai/generic.gif" border= "0" alt="未知类型" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/PyMOLmaterials_new.rar" target="_self" title="未知类型">
                        <span class="visible-sm-inline visible-xs-inline">PyMOLmaterials_new.rar</span>
                        <span class="hidden-sm hidden-xs">PyMOLmaterials_new.rar</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">PyMOLmaterials_new.rar 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/PyMOLmaterials_new.rar';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/PyMOLmaterials_new.rar';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:15
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							46.4 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list19" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/Structural Biology - Practical NMR Applications.pdf" /><label for="list19" class="skip">选择: Structural Biology - Practical NMR Applications.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Structural%20Biology%20-%20Practical%20NMR%20Applications.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/Structural%20Biology%20-%20Practical%20NMR%20Applications.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">Structural Biology - Prac ...</span>
                        <span class="hidden-sm hidden-xs">Structural Biology - Practical NMR Applications.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">Structural Biology - Practical NMR Applications.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Structural Biology - Practical NMR Applications.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/Structural Biology - Practical NMR Applications.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							2.7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list20" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/top_all36_prot.rtf" /><label for="list20" class="skip">选择: top_all36_prot.rtf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/top_all36_prot.rtf" target="_self">
																			<img src="/library/image/sakai/word.gif" border= "0" alt="RTF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/top_all36_prot.rtf" target="_self" title="RTF">
                        <span class="visible-sm-inline visible-xs-inline">top_all36_prot.rtf</span>
                        <span class="hidden-sm hidden-xs">top_all36_prot.rtf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">top_all36_prot.rtf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/top_all36_prot.rtf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/top_all36_prot.rtf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							71.5 KB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list21" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/topology-tutorial.pdf" /><label for="list21" class="skip">选择: topology-tutorial.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/topology-tutorial.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/topology-tutorial.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">topology-tutorial.pdf</span>
                        <span class="hidden-sm hidden-xs">topology-tutorial.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">topology-tutorial.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/topology-tutorial.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/topology-tutorial.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							4.4 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list22" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/蛋白质晶体学（IV）.pptx" /><label for="list22" class="skip">选择: &#34507;&#30333;&#36136;&#26230;&#20307;&#23398;&#65288;IV&#65289;.pptx</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%9B%8B%E7%99%BD%E8%B4%A8%E6%99%B6%E4%BD%93%E5%AD%A6%EF%BC%88IV%EF%BC%89.pptx" target="_self">
																			<img src="/library/image/sakai/ppt.gif" border= "0" alt="PowerPoint " hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%9B%8B%E7%99%BD%E8%B4%A8%E6%99%B6%E4%BD%93%E5%AD%A6%EF%BC%88IV%EF%BC%89.pptx" target="_self" title="PowerPoint ">
                        <span class="visible-sm-inline visible-xs-inline">&#34507;&#30333;&#36136;& ...</span>
                        <span class="hidden-sm hidden-xs">&#34507;&#30333;&#36136;&#26230;&#20307;&#23398;&#65288;IV&#65289;.pptx</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#34507;&#30333;&#36136;&#26230;&#20307;&#23398;&#65288;IV&#65289;.pptx 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/蛋白质晶体学（IV）.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/蛋白质晶体学（IV）.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							12.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list23" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/国科大 NMR技术应用（二）.pdf" /><label for="list23" class="skip">选择: &#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#20108;&#65289;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%BA%8C%EF%BC%89.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%BA%8C%EF%BC%89.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#22269;&#31185;&#22823;  ...</span>
                        <span class="hidden-sm hidden-xs">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#20108;&#65289;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#20108;&#65289;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（二）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（二）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							1.7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list24" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/国科大 NMR技术应用（三）.pdf" /><label for="list24" class="skip">选择: &#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19977;&#65289;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%B8%89%EF%BC%89.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%B8%89%EF%BC%89.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#22269;&#31185;&#22823;  ...</span>
                        <span class="hidden-sm hidden-xs">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19977;&#65289;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19977;&#65289;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（三）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（三）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							2.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list25" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/国科大 NMR技术应用（四）.pdf" /><label for="list25" class="skip">选择: &#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#22235;&#65289;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E5%9B%9B%EF%BC%89.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E5%9B%9B%EF%BC%89.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#22269;&#31185;&#22823;  ...</span>
                        <span class="hidden-sm hidden-xs">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#22235;&#65289;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#22235;&#65289;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（四）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（四）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							5.3 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list26" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/国科大 NMR技术应用（一）.pdf" /><label for="list26" class="skip">选择: &#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19968;&#65289;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%B8%80%EF%BC%89.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%B8%80%EF%BC%89.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#22269;&#31185;&#22823;  ...</span>
                        <span class="hidden-sm hidden-xs">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19968;&#65289;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#22269;&#31185;&#22823; NMR&#25216;&#26415;&#24212;&#29992;&#65288;&#19968;&#65289;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（一）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/国科大 NMR技术应用（一）.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							5.2 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list27" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/核磁共振技术-基本原理.pdf" /><label for="list27" class="skip">选择: &#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#22522;&#26412;&#21407;&#29702;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%90%86.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%90%86.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#26680;&#30913;&#20849;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#22522;&#26412;&#21407;&#29702;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#22522;&#26412;&#21407;&#29702;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-基本原理.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-基本原理.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							1.6 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list28" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/核磁共振技术-谱仪和实验操作.pdf" /><label for="list28" class="skip">选择: &#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#35889;&#20202;&#21644;&#23454;&#39564;&#25805;&#20316;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E8%B0%B1%E4%BB%AA%E5%92%8C%E5%AE%9E%E9%AA%8C%E6%93%8D%E4%BD%9C.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E8%B0%B1%E4%BB%AA%E5%92%8C%E5%AE%9E%E9%AA%8C%E6%93%8D%E4%BD%9C.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#26680;&#30913;&#20849;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#35889;&#20202;&#21644;&#23454;&#39564;&#25805;&#20316;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#35889;&#20202;&#21644;&#23454;&#39564;&#25805;&#20316;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-谱仪和实验操作.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-谱仪和实验操作.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							1.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list29" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/核磁共振技术-样品制备.pdf" /><label for="list29" class="skip">选择: &#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#26679;&#21697;&#21046;&#22791;.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E6%A0%B7%E5%93%81%E5%88%B6%E5%A4%87.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%A0%B8%E7%A3%81%E5%85%B1%E6%8C%AF%E6%8A%80%E6%9C%AF-%E6%A0%B7%E5%93%81%E5%88%B6%E5%A4%87.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#26680;&#30913;&#20849;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#26679;&#21697;&#21046;&#22791;.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26680;&#30913;&#20849;&#25391;&#25216;&#26415;-&#26679;&#21697;&#21046;&#22791;.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-样品制备.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/核磁共振技术-样品制备.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							299 KB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list30" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/计算结构生物学-Lecture1.pdf" /><label for="list30" class="skip">选择: &#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture1.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture1.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture1.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#35745;&#31639;&#32467;& ...</span>
                        <span class="hidden-sm hidden-xs">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture1.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture1.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture1.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture1.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							6 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list31" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/计算结构生物学-Lecture2.pdf" /><label for="list31" class="skip">选择: &#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture2.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture2.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture2.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#35745;&#31639;&#32467;& ...</span>
                        <span class="hidden-sm hidden-xs">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture2.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture2.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture2.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture2.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list32" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/计算结构生物学-Lecture3.pdf" /><label for="list32" class="skip">选择: &#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture3.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture3.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture3.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#35745;&#31639;&#32467;& ...</span>
                        <span class="hidden-sm hidden-xs">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture3.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture3.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture3.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture3.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							5.3 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list33" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/计算结构生物学-Lecture4.pdf" /><label for="list33" class="skip">选择: &#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture4.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture4.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6-Lecture4.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#35745;&#31639;&#32467;& ...</span>
                        <span class="hidden-sm hidden-xs">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture4.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#35745;&#31639;&#32467;&#26500;&#29983;&#29289;&#23398;-Lecture4.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture4.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/计算结构生物学-Lecture4.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							6.1 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list34" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/结构生物学技术排课 2019.pdf" /><label for="list34" class="skip">选择: &#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;&#25490;&#35838; 2019.pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6%E6%8A%80%E6%9C%AF%E6%8E%92%E8%AF%BE%202019.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E7%BB%93%E6%9E%84%E7%94%9F%E7%89%A9%E5%AD%A6%E6%8A%80%E6%9C%AF%E6%8E%92%E8%AF%BE%202019.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#32467;&#26500;&#29983;& ...</span>
                        <span class="hidden-sm hidden-xs">&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;&#25490;&#35838; 2019.pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#32467;&#26500;&#29983;&#29289;&#23398;&#25216;&#26415;&#25490;&#35838; 2019.pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/结构生物学技术排课 2019.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/结构生物学技术排课 2019.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:22
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							85.8 KB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list35" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/晶体学实践_Lecture II.pptx" /><label for="list35" class="skip">选择: &#26230;&#20307;&#23398;&#23454;&#36341;_Lecture II.pptx</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_Lecture%20II.pptx" target="_self">
																			<img src="/library/image/sakai/ppt.gif" border= "0" alt="PowerPoint " hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_Lecture%20II.pptx" target="_self" title="PowerPoint ">
                        <span class="visible-sm-inline visible-xs-inline">&#26230;&#20307;&#23398;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26230;&#20307;&#23398;&#23454;&#36341;_Lecture II.pptx</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26230;&#20307;&#23398;&#23454;&#36341;_Lecture II.pptx 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_Lecture II.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_Lecture II.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:16
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							2.8 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list36" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/晶体学实践_Lecture III_IV.pptx" /><label for="list36" class="skip">选择: &#26230;&#20307;&#23398;&#23454;&#36341;_Lecture III&amp;IV.pptx</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_Lecture%20III_IV.pptx" target="_self">
																			<img src="/library/image/sakai/ppt.gif" border= "0" alt="PowerPoint " hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_Lecture%20III_IV.pptx" target="_self" title="PowerPoint ">
                        <span class="visible-sm-inline visible-xs-inline">&#26230;&#20307;&#23398;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26230;&#20307;&#23398;&#23454;&#36341;_Lecture III&amp;IV.pptx</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26230;&#20307;&#23398;&#23454;&#36341;_Lecture III&amp;IV.pptx 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_Lecture III_IV.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_Lecture III_IV.pptx';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:18
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							38.7 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list37" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/晶体学实践_New_Lecture I.ppt" /><label for="list37" class="skip">选择: &#26230;&#20307;&#23398;&#23454;&#36341;_New_Lecture I.ppt</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_New_Lecture%20I.ppt" target="_self">
																			<img src="/library/image/sakai/ppt.gif" border= "0" alt="PowerPoint " hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E6%99%B6%E4%BD%93%E5%AD%A6%E5%AE%9E%E8%B7%B5_New_Lecture%20I.ppt" target="_self" title="PowerPoint ">
                        <span class="visible-sm-inline visible-xs-inline">&#26230;&#20307;&#23398;& ...</span>
                        <span class="hidden-sm hidden-xs">&#26230;&#20307;&#23398;&#23454;&#36341;_New_Lecture I.ppt</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#26230;&#20307;&#23398;&#23454;&#36341;_New_Lecture I.ppt 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_New_Lecture I.ppt';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/晶体学实践_New_Lecture I.ppt';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:18
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							11.5 MB 
						</td>
									</tr>
				 				 															
																				<tr 
					class="">
										<td headers="expansion" class="attach hidden-sm hidden-xs">
					</td>
					<td headers="checkboxes" class="attach">
													<input type="checkbox" name="selectedMembers" id="list38" 
																		onclick="adjustCount(this, 'copy');;adjustShowHideCount(this)"
 									value="/group/165118/实用数学手册_第2版_.pdf" /><label for="list38" class="skip">选择: &#23454;&#29992;&#25968;&#23398;&#25163;&#20876;(&#31532;2&#29256;).pdf</label>
							 							<input type="hidden" name="itemHidden" id="itemHidden" value="false" />
							<input type="hidden" name="itemCanRevise" id="itemCanRevise" value="false" />
											</td>
					<td style="text-indent:1em" class="specialLink title" scope="row">
					                            
              																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%AE%9E%E7%94%A8%E6%95%B0%E5%AD%A6%E6%89%8B%E5%86%8C_%E7%AC%AC2%E7%89%88_.pdf" target="_blank">
																			<img src="/library/image/sakai/pdf.gif" border= "0" alt="PDF" hspace="0" />
									</a>
																																											<a href="http://course.ucas.ac.cn/access/content/group/165118/%E5%AE%9E%E7%94%A8%E6%95%B0%E5%AD%A6%E6%89%8B%E5%86%8C_%E7%AC%AC2%E7%89%88_.pdf" target="_blank" title="PDF">
                        <span class="visible-sm-inline visible-xs-inline">&#23454;&#29992;&#25968;& ...</span>
                        <span class="hidden-sm hidden-xs">&#23454;&#29992;&#25968;&#23398;&#25163;&#20876;(&#31532;2&#29256;).pdf</span>
    									</a>
																								              					</td>
					<td headers="actions1"  style="white-space:nowrap;vertical-align:middle"  class="attach">
											</td>
					
					
					<td headers="actions2" class="attach actions2">
                        <div class="btn-group  pull-right">
                            <button type="button" class="btn resources-dropdown btn-xs" aria-expanded="false" data-toggle="dropdown" title="操作">
                                <span class="sr-only">&#23454;&#29992;&#25968;&#23398;&#25163;&#20876;(&#31532;2&#29256;).pdf 操作</span>
                                <span class="hidden-xs hidden-sm">操作</span>
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu row" role="menu">
	                            <li class="dropdown-button">
	                                <a href="" class="close-button"></a>
	                            </li>
                                                                                                                                    <li role="presentation" class="dropdown-header">操作</li>
                                    <li class="divider"></li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/实用数学手册_第2版_.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:copy';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            复制
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="#" role="menuitem" tabindex="-1" style="width:auto" onclick="document.getElementById('selectedItemId').value='/group/165118/实用数学手册_第2版_.pdf';document.getElementById('rt_action').value='org.sakaiproject.content.types.fileUpload:info';document.getElementById('sakai_action').value='doDispatchAction';submitform('showForm');">
                                            查看详细信息
                                        </a>
                                    </li>
                                                                                                </ul>
                        </div>
					</td>
											<td headers="access" class="hidden-sm hidden-xs access" title="整个站点可见">
							整个站点
						</td>
						<td headers="creator" class="creator hidden-sm hidden-xs">
							&#21494;&#20811;&#31351;
						</td>
						<td headers="modified" class="modified hidden-sm hidden-xs">
							2019-9-3 下午5:18
						</td>
						<td headers="size" class="size hidden-sm hidden-xs">
							162.3 MB 
						</td>
									</tr>
				 				 			 		
																	
		</table>
		<div id="bottompadding" style="height:35em"> </div> 
		
					<input type="hidden" id="copy-count" value="0" />
				<input type="hidden" name="sakai_csrf_token" value="59949484946c9da2d2b4deb623bba3facf7e0c62a8a92f28431fa3738e45cc5e" />
		<input type="hidden" id="show-count" value="0" />
		<input type="hidden" id="hide-count" value="0" /> 
				<input type="hidden" id="copy-count-other" value="0" />
	</form>						
</div>
<script type="text/JavaScript">
	<!--
												document.getElementById("selectall").disabled = false;
		
		jQuery(function() {
			jQuery("#dialog-copyright").dialog({
				resizable: false,
				autoOpen: false,
				height:300,
				width:600,
				modal: true
			});
		});

		function openCopyrightWindow(url,winName,winSettings) {
			//Idea from http://stackoverflow.com/q/16086162/3708872
			jQuery.ajax({
				type: "GET",
				url: url,
				dataType: "html",
				success: function(response, status, request) {
					var disp = request.getResponseHeader('Content-Disposition');
					//Might just want to do attachments, but for now put everything in a new window
					if (disp) {
						var form = jQuery('<form method="GET" action="' + url + '" target="_blank">');
						jQuery('body').append(form);
						form.submit();
					} 
					else {
						jQuery.get(url, function(data, textStatus, jqXHR){
							jQuery('#dialog-copyright').html(data);
							jQuery('#dialog-copyright').dialog('open');
						}, "html");
					}

					return false;
				},
			error: function (xhr, ajaxOptions, thrownError) {
				window.console && console.log("Error from GET request"+thrownError);
				
			}
			});
		};

		function toggleSelectAll(caller, elementName)
		{
			var newValue = caller.checked;
			var elements = document.getElementsByName(elementName);
			
			if(elements)
			{
				for(var i = 0; i < elements.length; i++)
				{
					elements[i].checked = newValue;
				}
			}
			
			if(newValue == true)
			{
				caller.title = "全部取消";
									var copy_button = document.getElementById("copy-button");
					if(copy_button)
					{
						copy_button.disabled = false;
						//let bd take care of this copy_button.className = 'enabled';
					}
					document.getElementById("copy-count").value = "37";
				                var show_button = document.getElementById("show-button");
                if(show_button) {
                        show_button.disabled = false;
                        //let bd take care of this show_button.className = 'enabled';
                }
                document.getElementById("show-count").value = "0";
                var hide_button = document.getElementById("hide-button");
                if(hide_button) {
                        hide_button.disabled = false;
                        //let bd take care of this hide_button.className = 'enabled';
                }
                document.getElementById("hide-count").value = "0";
			}
			else
			{
				caller.title = "全部选择";
									var copy_button = document.getElementById("copy-button");
					if(copy_button)
					{
						copy_button.disabled = true;
						//let bd take care of this copy_button.className = 'disabled';
					}
					document.getElementById("copy-count").value = "0";
				                var show_button = document.getElementById("show-button");
                if(show_button)
                {
                        show_button.disabled = true;
                        //let bd take care of this show_button.className = 'disabled';
                }
                document.getElementById("show-count").value = "0";
                var hide_button = document.getElementById("hide-button");
                if(hide_button)
                {
                        hide_button.disabled = true;
                        //let bd take care of this hide_button.className = 'disabled';
                }
                document.getElementById("hide-count").value = "0";
			}
		}
		
		function adjustCount(caller, key)
		{
			var counter = document.getElementById(key + "-count");
			var button = document.getElementById(key + "-button");
			
			if(caller && caller.checked && caller.checked == true)
			{
				counter.value = parseInt(counter.value) + 1;
			}
			else
			{
				counter.value = parseInt(counter.value) - 1;
			}
	
			if(button)
			{
				if(counter.value > 0)
				{
					button.disabled = false;
					//let bd take care of this button.className='enabled';
				}
				else
				{
					button.disabled = true;
					//let bd take care of this button.className='disabled';
				}
			}
		}

		function adjustCountOther(caller, key) {
			var counter = document.getElementById(key + "-count-other");
			var button = document.getElementById(key + "-button-other");
			if (caller && caller.checked && caller.checked == true) {
				counter.value = parseInt(counter.value) + 1;
			} else {
				counter.value = parseInt(counter.value) - 1;
			}
			if (button) {
				if (counter.value > 0) {
					button.disabled = false;
					//let bd take care of this: button.className='enabled';
				} else {
					button.disabled = true;
					//let bd take care of this: button.className='disabled';
				}
			}
		}

   function adjustShowHideCount(caller) {
                var trlist = caller.parentNode.parentNode.parentNode.childNodes;
                var enableshow=  false ;
                var enablehide=  false ;

                for (var i=0; i<trlist.length; i++){
                        var thisTR = trlist[i];
                        if (thisTR.tagName == "TR"){
                                var inputlist= thisTR.getElementsByTagName("input");
                                if (inputlist.length ==3) {

                                        // 1.  check itemHidden
                                        var thisTRitemHidden= thisTR.getElementsByTagName("input")[1];

                                        var currHidden = false;
                                        if (thisTRitemHidden&& (thisTRitemHidden.name == "itemHidden")) {
                                                currHidden= thisTRitemHidden.value;
                                        }

                                        // 2. check itemCanRevise
                                        var thisTRitemCanRevise = thisTR.getElementsByTagName("input")[2];
                                        var currCanRevise= false;
                                        if (thisTRitemCanRevise && (thisTRitemCanRevise.name == "itemCanRevise")) {
                                                currCanRevise= thisTRitemCanRevise.value;
                                        }

                                        // 3. check item is checked or not
                                        var thisTRcheckbox = thisTR.getElementsByTagName("input")[0];
                                        var currchecked = false;
                                        if (thisTRcheckbox && (thisTRcheckbox.name == "selectedMembers")) {
                                                currchecked = thisTRcheckbox.checked;
                                        }


                                        if ((currchecked==true) && (currHidden=="true") && (currCanRevise == "true")) {
                                                enableshow= true;
                                                break;
                                        }
                                }
                        }
                }
                for (var i=0; i<trlist.length; i++){
                        var thisTR = trlist[i];
                        if (thisTR.tagName == "TR"){
                                var inputlist= thisTR.getElementsByTagName("input");
                                if (inputlist.length ==3) {

                                        // 1.  check itemHidden
                                        var thisTRitemHidden= thisTR.getElementsByTagName("input")[1];
                                        var currHidden = false;
                                        if (thisTRitemHidden&& (thisTRitemHidden.name == "itemHidden")) {
                                                currHidden= thisTRitemHidden.value;
                                        }

                                        // 2. check itemCanRevise
                                        var thisTRitemCanRevise = thisTR.getElementsByTagName("input")[2];
                                        var currCanRevise= false;
                                        if (thisTRitemCanRevise && (thisTRitemCanRevise.name == "itemCanRevise")) {
                                                currCanRevise= thisTRitemCanRevise.value;
                                        }

                                        // 3. check item is checked or not
                                        var thisTRcheckbox = thisTR.getElementsByTagName("input")[0];
                                        var currchecked = false;
                                        if (thisTRcheckbox && (thisTRcheckbox.name == "selectedMembers")) {
                                                currchecked = thisTRcheckbox.checked;
                                        }

                                        if ((currchecked==true) && (currHidden=="false") && (currCanRevise == "true")) {
                                                enablehide= true;
                                                break;
                                        }
                                }
                        }
                }

                var showbutton = document.getElementById("show-button");
                if(showbutton)
                {
                        if (enableshow)
                        {
                                showbutton.disabled = false;
                                //let bd take care of this: showbutton.className='enabled';
                        }
                        else
                        {
                                showbutton.disabled = true;
                                //let bd take care of this: showbutton.className='disabled';
                        }
                }

                var hidebutton = document.getElementById("hide-button");
                if(hidebutton)
                {
                        if (enablehide)
                        {
                                hidebutton.disabled = false;
                                //let bd take care of this: hidebutton.className='enabled';
                        }
                        else
                        {
                                hidebutton.disabled = true;
                                //let bd take care of this: hidebutton.className='disabled';
                        }
                }
        }

		function disableLinks()
		{
			if(document.getElementsByName)
			{
				var enabledLinks = document.getElementsByName("enabledActionLinks");
				var disabledLinks = document.getElementsByName("disabledActionLinks");
				if(enabledLinks)
				{
					for(var i = 0; i < enabledLinks.length; i++)
					{
						//enabledLinks[i].innerHTML = disabledLinks[i].innerHTML;
						enabledLinks[i].style.display="none";
						disabledLinks[i].style.display="block";
					}
				}			
			}
		}
		function submitform(id)
		{
			var theForm = document.getElementById(id);
			if(theForm && theForm.onsubmit)
			{
				theForm.onsubmit();
			}
			if(theForm && theForm.submit)
			{
				theForm.submit();
			}
		}
    
    $('ul.makeMenu').keydown(function(e) { // "Add" and "Action" menus keyboard interaction handler
	if(e.target.nodeName.toLowerCase() == 'li') {
	    // Must be an 'add' or 'action' li
	    switch(e.which) {
		case 38: // up arrow
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    $('.makeMenuChild').hide();
		    $(e.target).find('.makeMenuChild').show().find('li:last a').first().focus();
		    break;
		case 13: // enter
		case 32: // space
		case 40: // down arrow
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    $('.makeMenuChild').hide();
		    $(e.target).find('.makeMenuChild').show().find('li:first a').first().focus();
		    break;
		case 9:
		    $('.makeMenuChild').hide();
		    break;
	    }
	} else {
	    // If not a li element, must be a submenu link (nothing else can have keyboard focus)
	    switch(e.which) {
		case 32: // space
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    window.location.href = e.target.href; // .trigger('click') didn't work on the anchors, this does though
		    break;
		case 38: // up arrow -- does not wrap around
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    $(e.target).parent('li').prev('li').find('a').first().focus();
		    break;
		case 40: // down arrow -- does not wrap around
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    $(e.target).parent('li').next('li').find('a').first().focus();
		    break;
		case 9: // tab key
		    // don't stop propagation or default, let browser move the focus!
		    $('.makeMenuChild').hide();
		    break;
		case 27: // esc key
		    e.preventDefault();
		    e.stopImmediatePropagation();
		    $('.makeMenuChild').hide();
		    $(e.target).parents('ul.makeMenu > li').first().focus();
		    break;
	    }
	}
    });

		
	//-->
</script>

	

                        <!-- End Buffered Body Tool Content -->

                     
                    <!-- end Tool Body -->
                    
                    </div>

                    <!-- end Tool Container -->

                 
             
        </div>

         
    </main> <!-- END of main.Mrphs-mainContent -->

<!-- END VM includePageBody.vm -->        
        <div class="Mrphs-container Mrphs-container--footer">

    
        
        <div class="Mrphs-container Mrphs-container--extras">

        
    <div id="Mrphs-footerApp">

        
            <div id="Mrphs-footerApp__chat" class="Mrphs-footerApp__portalChat is-hidden">
                <a href="#" id="Mrphs-footerApp--toggle" class="Mrphs-footerApp--toggle Mrphs-footerApp--toggle-chat">
                    <i class="Mrphs-footerApp--icon icon-sakai-chat"></i>
                    聊天 
                    <span id="Mrphs-footerApp--count" class="Mrphs-footerApp--count Mrphs-footerApp--count-chat"></span>
                </a>
                <!-- chat tray, will hold chat containers (as many as ongoing chats) -->
            </div>

         
    </div>

 

    <h1 class="skip">当前用户从此开始</h1>

    
        <span id="Mrphs-portalChat__avatar--permitted" class="skip"></span>

     
    <div id="Mrphs-portalChat" tabindex="-1" class="Mrphs-portalChat">

        <header id="Mrphs-portalChat__title" class="Mrphs-portalChat__title">聊天
            <a href="#" id="Mrphs-portalChat__close" title="关闭聊天" class="Mrphs-closeButton Mrphs-portalChat__close">
                <i class="Mrphs-footerApp--icon icon-sakai-close"></i>
                <span class="skip">关闭聊天</span>
            </a>
        </header>

   

    
        <div style="display:none;" id="Mrphs-portalChat__video--localcontent" class="Mrphs-portalChat__container Mrphs-portalChat__video--localcontent" data-video="0">
        
            <video id="Mrphs-portalChat__video--localvideo" class="pc_chat_video_min Mrphs-portalChat__videochat--video" autoplay muted="true"></video>
        
            <nav id="Mrphs-portalChat__video--nav">
                <a href="javascript:;" id="disable_local_video" onclick="return portal.chat.video.disableVideo();" title="禁用您的视频" class="Mrphs-portalChat__videochat--videobutton">
                	<i class="Mrphs-footerApp--icon icon-sakai-videocam"></i>
                	<i class="Mrphs-footerApp--icon icon-sakai-toggle-on"></i>
                </a>
                <a href="javascript:;" id="enable_local_video" onclick="return portal.chat.video.enableVideo();" style="display:none" title="启用您的视频" class="Mrphs-portalChat__videochat--videobutton">
                	<i class="Mrphs-footerApp--icon icon-sakai-videocam"></i>
                	<i class="Mrphs-footerApp--icon icon-sakai-toggle-off"></i>
                </a>
                <a href="javascript:;" id="mute_local_audio" onclick="return portal.chat.video.mute();"  title="静音" class="Mrphs-portalChat__videochat--videobutton ">
                	<i class="Mrphs-footerApp--icon icon-sakai-mic"></i>
                	<i class="Mrphs-footerApp--icon icon-sakai-toggle-on"></i>
                
                </a>
                <a href="javascript:;" id="unmute_local_audio" onclick="return portal.chat.video.unmute();" style="display:none" title="取消静音" class="Mrphs-portalChat__videochat--videobutton">
                	<i class="Mrphs-footerApp--icon icon-sakai-mic"></i>
                	<i class="Mrphs-footerApp--icon icon-sakai-toggle-off"></i>
                
                </a>
            </nav>
        
        </div>
	 	    <div id="Mrphs-portalChat__content" class="Mrphs-portalChat__container Mrphs-portalChat__content">
	    
	        <ul id="pc_options" class="Mrphs-portalChat__list Mrphs-portalChat__options">
	
	            <li id="pc_show_off_ctrl" class="Mrphs-portalChat__options--list-item">
	                <input type="checkbox" id="Mrphs-portalChat__showoffline" class="Mrphs-portalChat__options--checkbox">
	                <label for="Mrphs-portalChat__showoffline" class="Mrphs-portalChat__options--label Mrphs-portalChat__options--showoffline">显示离线好友</label>
	            </li>       
	
	            <li id="pc_go_off_ctrl" class="Mrphs-portalChat__options--list-item">
	                <input type="checkbox" id="Mrphs-portalChat__gooffline--check" class="Mrphs-portalChat__checkbox Mrphs-portalChat__checkbox--options">
	                <label for="Mrphs-portalChat__gooffline--check" class="Mrphs-portalChat__options--label Mrphs-portalChat__options--go-offline">显示为离线</label>
	            </li>
	
	            	                <li id="Mrphs-portalChat__videooff--ctrl" class="Mrphs-portalChat__options--list-item">
	                    <input type="checkbox" id="Mrphs-portalChat__videooff--check" class="Mrphs-portalChat__options--checkbox">
	                    <label for="Mrphs-portalChat__videooff--check" class="Mrphs-portalChat__options--label Mrphs-portalChat__options--video-off">禁用视频</label>
	                </li>
	
	             	
	        </ul>
	
	        <div id="Mrphs-portalChat__users" class="Mrphs-portalChat__container Mrphs-portalChat__users">
	
	            <div id="Mrphs-portalChat__connections--wrapper" class="Mrphs-portalChat__connections--wrapper">
	                <h2 class="Mrphs-portalChat__title">我的好友</h2>
	                <ul id="Mrphs-portalChat__connections" class="Mrphs-portalChat__list Mrphs-portalChat__connections"></ul>
	            </div>
	
	            <div class=".Mrphs-portalChat__user--wrapper" >
	                <h2 class="Mrphs-portalChat__title">在此站点</h2>
	                <ul id="Mrphs-portalChat__siteusers"class="Mrphs-portalChat__list Mrphs-portalChat__siteusers"></ul>
	            </div>
	
	        </div>
	
	    </div>
	</div>
    <!-- Trimpath template for the profile connections list --> 
    <div id="pc_connections_template" class="Mrphs-portalChat__template Mrphs-portalChat__template--connections is-hidden"><!--
                {for connection in connections}
                    <li class="Mrphs-portalChat_connection Mrphs-portalChat__list-item" >

                        <a id="${connection.uuid}_link" class="Mrphs-portalChat__user--link" href="javascript:;" onclick="return portal.chat.setupChatWindow('${connection.uuid}');">
										                            <img class="Mrphs-portalChat__image Mrphs-portalChat__user--image" src="/direct/profile/${connection.uuid}/image"/>
			                            <span class="Mrphs-portalChat__user--name">${connection.displayName}</span>
                            {if connection.online}
         	                   {if connection.video == 'none' || !portal.chat.video || !portal.chat.video.webrtc.isVideoEnabled()}
                           	       <i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-online"></i>
                               {/if}
                            {else}
                            	<i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-offline"></i>
                            {/if}
                        </a>
                        {if connection.online}
     	                   {if connection.video != 'none' && portal.chat.video && portal.chat.video.webrtc.isVideoEnabled()}
	                        <a id="${connection.uuid}_link" class="Mrphs-portalChat__connection--videolink" href="javascript:;" onclick="return portal.chat.video.directVideoCall('${connection.uuid}',false);">
                        	   <i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-videocam"></i>
                        	</a>
                           {/if}
                        {/if}
                        {if connection.online == false}
                            <a href="javascript:;" onclick="portal.chat.pingConnection('${connection.uuid}');" title="Ping ${connection.displayName} 获取连接进行聊天">
                           	   <i class=" Mrphs-footerApp--icon icon-sakai-bell"></i>
                            </a>
                       		<span id="Mrphs-portalChat__connection--ping_${connection.uuid}" class=" Mrphs-portalChat__connection--ping ">Ping成功！</span>
                        {/if}
                    </li>
                {/for}
            -->

    </div>

    <!-- Trimpath template for the present users list -->
    <div id="pc_site_users_template" class="Mrphs-portalChat__template Mrphs-portalChat__template--users is-hidden"><!--
                {for user in siteUsers}
                    <li class="Mrphs-portalChat__user Mrphs-portalChat__list-item">
                        {if !user.offline}
                        <a id="${user.id}_link" class="pc_user_link Mrphs-portalChat__user--link" href="javascript:;" onclick="return portal.chat.setupChatWindow('${user.id}');">
                        {/if}
										                            <img class="pc_user_image Mrphs-portalChat__image Mrphs-portalChat__user--image" src="/direct/profile/${user.id}/image" />
			                            <span class="pc_site_display_name Mrphs-portalChat__name Mrphs-portalChat__user--name">${user.displayName}</span>
                            {if user.offline == false}
                              {if user.video == 'none' || !portal.chat.video || !portal.chat.video.webrtc.isVideoEnabled()}
                           	       <i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-online"></i>
                              {/if}
                            {else}
                           	       <i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-offline"></i>
                            {/if}
                        {if user.offline == false}
                        </a>
                        {/if}
                        {if user.video != 'none' && portal.chat.video && portal.chat.video.webrtc.isVideoEnabled()}
                         <a id="${user.id}_link" class="Mrphs-portalChat__connection--videolink" href="javascript:;" onclick="return portal.chat.video.directVideoCall('${user.id}',false);">
                        	   <i class="Mrphs-portalChat__connection--bullet Mrphs-footerApp--icon icon-sakai-videocam"></i>
                         </a>
                        {/if}
                    </li>
                {/for}
            -->
    </div>

    <!-- Trimpath template for the chat windows -->
    <div id="pc_connection_chat_template" class="Mrphs-portalChat__template Mrphs-portalChat__template--chat is-hidden" tabindex="-1"><!--
               <div class="pc_connection_chat_title_avt pc_connection_chat_title Mrphs-portalChat__chat--title Mrphs-portalChat__chat--titleavt" onclick="portal.chat.toggleChatWindow('${uuid}');"><a href="#">
                 <img src="/direct/profile/${uuid}/image" class="pc_connection_chat_title_avt Mrphs-portalChat__user--image"/><span class="Mrphs-portalChat__user--name">${displayName}</span></a>
                    <a href="javascript:;" class="Mrphs-portalChat__close" onclick="return portal.chat.closeChatWindow('${uuid}');" title="关闭聊天">
						<i class="Mrphs-footerApp--icon icon-sakai-close"></i>
						<span class="skip">关闭聊天</span>
					</a>
                </div>
                				<div id="Mrphs-portalChat__chat--videochatbar-${uuid}" class="pc_connection_videochat_bar Mrphs-portalChat__videochat--bar Mrphs-portalChat__videochat--ctrlbar">
					<div class="Mrphs-portalChat__videochat--barelement Mrphs-portalChat__videochat--leftelement">
						<a href="javascript:;" onclick="return portal.chat.video.openVideoCall('${uuid}',false);" class="video_off Mrphs-portalChat__videochat--videobutton " title="发起视频聊天" >
							<i class="Mrphs-footerApp--icon icon-sakai-videocam"></i>
						</a>
						<a href="javascript:;" onclick="return portal.chat.video.closeVideoCall('${uuid}',true);" class="video_on Mrphs-portalChat__videochat--videobutton" title="结束视频聊天" >
								<i class="Mrphs-footerApp--icon icon-sakai-stop"></i>
						</a>
						<a href="javascript:;" onclick="return portal.chat.video.maximizeVideoCall('${uuid}');" class="video_on Mrphs-portalChat__videochat--videobutton" title="最大化视频聊天" >
							<i class="Mrphs-footerApp--icon icon-sakai-maximize"></i>
						</a>
					</div>
					<div id="Mrphs-portalChat__chat--videoin-${uuid}" class="pc_connection_videochat_bar_answer Mrphs-portalChat__videochat--barelement Mrphs-portalChat__videochat--answerelement">
						<a href="javascript:;" onclick="return portal.chat.video.acceptVideoCall('${uuid}');" class="Mrphs-portalChat__videochat--videobutton" title="接收视频聊天">
							<i class="Mrphs-footerApp--icon icon-sakai-thumbup"></i>
						</a>
						<a href="javascript:;" onclick="return portal.chat.video.ignoreVideoCall('${uuid}');" class="Mrphs-portalChat__videochat--videobutton" title="忽略视频聊天">
							<i class="Mrphs-footerApp--icon icon-sakai-thumbdown"></i>
						</a>
						<span>您想应答吗？</span>
					</div>
					<div id="Mrphs-portalChat__chat--videotime-${uuid}" class=" Mrphs-portalChat__videochat--barelement Mrphs-portalChat__videochat--rightelement">
						<span id="Mrphs-portalChat__chat--time-${uuid}">00:00</span>
					</div>
                </div>
				<div id="Mrphs-portalChat__chat--videocontent-${uuid}" class="Mrphs-portalChat__chat--videocontent">
					<div style="display:none;" class="Mrphs-portalChat__videochat--statusbar "><span></span></div>
					<div style="display:none;" class="Mrphs-portalChat__videochat--statuselement Mrphs-portalChat__videochat--statusfailed" ><i class="Mrphs-footerApp--icon icon-sakai-frown"></i></div>
					<div style="display:none;" class="Mrphs-portalChat__videochat--statuselement Mrphs-portalChat__videochat--statusfinished" ><i class="Mrphs-footerApp--icon icon-sakai-flagcheckered"></i></div>
					
					<div style="display:none;" class="Mrphs-portalChat__videochat--statuselement Mrphs-portalChat__videochat--bubblingG">
						<span class="Mrphs-portalChat__videochat--bubblingG_1">
						</span>
						<span class="Mrphs-portalChat__videochat--bubblingG_2">
						</span>
						<span class="Mrphs-portalChat__videochat--bubblingG_3">
						</span>
					</div>
					
					<div style="display:none;" class="Mrphs-portalChat__videochat--statuselement Mrphs-portalChat__videochat--remotevideo">
						<video id="Mrphs-portalChat__videochat--remotevideo-${uuid}" class="Mrphs-portalChat__videochat--video " autoplay >
						</video>
					</div>

				</div>
				                <div id="Mrphs-portalChat__chat--content-${uuid}" class="pc_connection_chat_content Mrphs-portalChat__chat--content">
                    <ul id="Mrphs-portalChat__chat--messages-${uuid}" class="Mrphs-portalChat__chat--messages"></ul>
                    <div class="Mrphs-portalChat__chat--editorwrapper"><input type="text" id="Mrphs-portalChat__chat--editor-${uuid}" class="Mrphs-portalChat__chat--editor" alt="" title="输入聊天内容"/></div>
                </div>
            -->
    </div> 



    <!-- Chat windows get prepended to this container -->
    <div class="Mrphs-portalChat__chat--container"><div class="Mrphs-portalChat__chat--windowscroller"></div></div>
    <!-- END FLOATING CHAT STUFF -->

 
 
        </div>         <div id="tutorial" class="Mrphs-tutorial Mrphs-modal"></div>

     
</div>
    </div>
    
    </div>
    

</div>

    
<!-- END VM includePageWithNav.vm -->

        </div> <!-- end Mrphs-portalWrapper -->
        <!-- END VM site.vm -->

            <script>
        var needJQuery = true;
        var secondJQuery = false;
        var notJQuery = false;
        var dollarEmpty = false;
        var dollarVersion = false;
        if ( window.$ ) {
              if ( window.$.fn && window.$.fn ) {
                 dollarVersion = window.$.fn.jquery;
              } else {
                 dollarVersion = 'not jQuery';
                 window.console && console.log('Dollar is defined but is not jQuery');
                 window.console && console.log($);
                 //Just have it reload this other $ afterward
                 notJQuery = true;
              }
         } else {
              dollarEmpty = true;
              dollarVersion = 'not present';
              if ( window.jQuery ) {
                  window.console && console.log('tool called jQuery.noConflict()');
              }
        }
        if ( window.jQuery ) {
            tver = jQuery.fn.jquery;
            if ( tver.indexOf('1.11.') == 0 ) {
                window.console && console.log('Using tool jQuery '+tver);
                needJQuery = false;
            } else {
                secondJQuery = true;
            }
        }
        if ( needJQuery ) {
            document.write('\x3Cscript src="/library/webjars/jquery/1.11.3/jquery.min.js?version=5c5a648">'+'\x3C/script>')
            document.write('\x3Cscript src="/library/webjars/jquery-migrate/1.4.0/jquery-migrate.min.js?version=5c5a648">'+'\x3C/script>')
            document.write('\x3Cscript src="/library/webjars/bootstrap/3.3.6/js/bootstrap.min.js?version=5c5a648">'+'\x3C/script>')
            document.write('\x3Cscript src="/library/webjars/jquery-ui/1.11.3/jquery-ui.min.js?version=5c5a648">'+'\x3C/script>')
            document.write('\x3Clink rel="stylesheet" href="/library/webjars/jquery-ui/1.11.3/jquery-ui.min.css?version=5c5a648"/>')
            if (Modernizr.touch) {
              document.write('\x3Cscript type="text/javascript" src="/library/webjars/jquery-ui-touch-punch/0.2.3/jquery.ui.touch-punch.min.js?version=5c5a648">'+'\x3C/script>')
            }
            window.console && console.log('Portal scripts loaded JQ+MI+BS+UI');
        } else {
            if (typeof jQuery.migrateWarnings == 'undefined') {
                document.write('\x3Cscript type="text/javascript" src="/library/webjars/jquery-migrate/1.4.0/jquery-migrate.min.js?version=5c5a648">'+'\x3C/script>')
                window.console && console.log('Portal adding jQuery migrate');
            }
            if ( typeof jQuery.fn.popover == 'undefined') {
                document.write('\x3Cscript type="text/javascript" src="/library/webjars/bootstrap/3.3.6/js/bootstrap.min.js?version=5c5a648">'+'\x3C/script>')
                window.console && console.log('Portal adding Bootstrap');
            }
            if (typeof jQuery.ui == 'undefined') {
                document.write('\x3Cscript type="text/javascript" src="/library/webjars/jquery-ui/1.11.3/jquery-ui.min.js?version=5c5a648">'+'\x3C/script>')
		document.write('\x3Clink rel="stylesheet" href="/library/webjars/jquery-ui/1.11.3/jquery-ui.min.css?version=5c5a648"/>')
                window.console && console.log('Portal adding jQuery UI');
            }
            if (typeof jQuery.ui == 'undefined' || (typeof jQuery.ui.mouse != 'undefined' && typeof jQuery.ui.mouse.prototype._touchStart == 'undefined')) {
                document.write('\x3Cscript type="text/javascript" src="/library/webjars/jquery-ui-touch-punch/0.2.3/jquery.ui.touch-punch.min.js?version=5c5a648">'+'\x3C/script>')
                window.console && console.log('Portal adding jQuery UI Touch Punch for touch device support');
            }
        }
    </script>
    <script>
        $PBJQ = jQuery; // The Portal's jQuery (also in $ for now)
    </script>

                    <script src="/portal/scripts/sessionstoragemanager.js?version=5c5a648"></script>
                 
        <!--[if lt IE 9]>
            <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.min.js"></script>
<![endif]-->

        <script src="/library/js/trimpath-template-latest.js?version=5c5a648"></script>
        <script src="/library/js/jquery/bgiframe/jquery.bgiframe.min.js?version=5c5a648"></script>
        <script src="/library/js/jquery/cluetip/1.2.10/jquery.cluetip.min.js?version=5c5a648"></script>
        <script src="/library/skin/morpheus-default/js/morpheus.plugins.min.js?version=5c5a648"></script>
        <script src="/library/skin/morpheus-default/js/morpheus.scripts.min.js?version=5c5a648"></script>
        <script src="/library/webjars//pnotify/2.1.0/pnotify.core.min.js?version=5c5a648"></script>
        <script src="/library/js/jquery/qtip/jquery.qtip-latest.min.js?version=5c5a648"></script>
        <script src="/library/js/jquery/qtip/tutorial.js?version=5c5a648"></script>

         
        

<script src="/portal/scripts/jquery.idle-timer.js?version=5c5a648" ></script>
<script>
	var portalChatPollInterval = 5000;
</script>

<script type="text/javascript">
    portal.chat.video.enabled = true;
    portal.chat.video.timeout = 25;
    portal.chat.video.messages = {
        "pc_video_status_setup": "设置您的视频……",
        "pc_video_status_user_hung": "用户以挂断",
        "pc_video_status_hangup": "您已挂断！",
        "pc_video_status_user_refused": "用户拒绝了您的请求",
        "pc_video_status_incoming_call": "您有一个连接请求……",
        "pc_video_status_call_timeout": "聊天发起超时！",
        "pc_video_status_waiting_peer": "等待连接……",
        "pc_video_status_call_accepted": "发起被接受，建立连接中……",
        "pc_video_status_call_not_accepted": "视频聊天没有被接受或连接失败",
        "pc_video_status_call_in_progress": "发起进行中……",
        "pc_video_status_answer_timeout": "应答超时！",
        "pc_video_status_connecting": "连接中……",
        "pc_video_status_connection_established": "连接已建立",
        "pc_video_status_call_failed": "发起失败",
        "pc_video_status_you_ignored": "您忽略了那个请求",
        "pc_video_status_connection_established": "连接已建立"
    };
</script>
<script type="text/javascript" src="/portal/scripts/webrtc-adapter.js?version=5c5a648"></script>
<script type="text/javascript" src="/portal/scripts/videocall.js?version=5c5a648"></script>

 
<script type="text/javascript" src="/portal/scripts/jescape.js?version=5c5a648"></script>
<script src="/portal/scripts/chat.js?version=5c5a648"></script>

 
         
                    <script>
                var sakaiPortalWindow = "";
                $PBJQ(document).ready(function() {
                    setupSkipNav();
                });
            </script>
         
        <script>
            // If we loaded a second jQuery, revert $ and jQuery to the first jQuery
            if ( secondJQuery ) {
                $PBJQ = jQuery.noConflict(true); // Safely return $ to the tool jQuery
                if ( ! dollarEmpty && !notJQuery ) jQuery = $;  // Return jQuery to point at the tool jQuery
            }
            if (notJQuery && !secondJQuery) {
                $PBJQ = jQuery.noConflict(true); // Safely return $ to the tool jQuery
                //Just set jQuery to be the same thing since it didn't exist before
                jQuery = $PBJQ;

            }
            window.console && console.log('Portal script load complete PBJQ='+$PBJQ.fn.jquery+' jQuery='+jQuery.fn.jquery+' $='+dollarVersion);

            $PBJQ(document).ready(function() {
                setupSiteNav();
                            });
        </script>

        <script>
        PNotify.prototype.options.styling = "jqueryui";
        function portal_check_pnotify() {
            $PBJQ.getJSON( "/direct/portal/notify.json", function( data ) {
                for(i=0; i<data.error.length; i++ ) {
                     $PBJQ(function(){
                        new PNotify({
                            title: '注意',
                            text: data.error[i],
                            type: 'notice'
                        });
                    });
                }
            });
        }
            </script>

        <!--[if lt IE 9]>
        <script src="/library/skin/morpheus-default/js/ie/sakai.portal.ie.js?version=5c5a648"></script>
<![endif]-->
 
         
         <link href="/pasystem-tool/stylesheets/pasystem.css?version=5c5a648" rel="stylesheet" property="stylesheet" type="text/css" />

<script>
// Work around the fact that several pages pull in very old versions
// of JQuery.
function paSystemJQueryOK() {
    if (!window.jQuery) {
        /* no jQuery at all */
        return false;
    }

    var version_numbers = jQuery.fn.jquery.split('.');

    /* >= 1.9+ */
    return (parseInt(version_numbers[0]) > 1) || (parseInt(version_numbers[0]) == 1 && parseInt(version_numbers[1]) >= 9);
}

if (paSystemJQueryOK()) {
  document.write('\x3Cscript src="/pasystem-tool/scripts/pasystem.js?version=5c5a648">\x3C/script>');
  document.write('\x3Cscript type="text/javascript" src="/pasystem-tool/scripts/featherlight.min.js?version=5c5a648">\x3C/script>');

  var pasystem = pasystem || {'loaded': true};
} else {
  console.log("PASystem not loaded for this page because jQuery is missing or unsupported.");
}
</script>
<script id="pasystemBannerAlertsTemplate" type="text/template">
  <div class="pasystem-banner-alert pasystem-banner-${type}" id="${id}">
    <span class="pasystem-banner-alert-message">${message}</span>
    {if dismissible}<a class="pasystem-banner-alert-close" href="javascript:void(0)"></a>{/if}
  </div>
</script>
<script id="pasystemBannerAlertsToggleTemplate" type="text/template">
  <li class="pasystem-banner-alert-toggle-list-item">
    <a href="javscript:void(0)" class="pasystem-banner-alert-toggle">
      显示系统广播
    </a>
  </li>
</script>
<script>
  if (pasystem) {
    pasystem['banners'] = new PASystemBannerAlerts([], "59949484946c9da2d2b4deb623bba3facf7e0c62a8a92f28431fa3738e45cc5e");
  }
</script>
<script type="text/template" id="popup-container-content">

</script>

<script type="text/template" id="popup-container-footer">
<div class="popup-container-footer">
  <a href="javascript:void(0)" class="popup-dismiss-button permanent" id="popup-acknowledged-button">不再显示</a>
  <a href="javascript:void(0)" class="popup-dismiss-button temporary" id="popup-later-button">稍后通知我</a>
</div>
</script>


<script id="timezoneBannerTemplate" type="text/template">
  <span>
    您的计算机设置的时区<span class="computerTimezone">${reportedTimezone}</span>和您的账户时区<span class="prefsTimezone">${prefsTimezone}</span>不一致。 <span class="pasystem-tz-click-here"><a href="${setTimezoneUrl}" id="setTimezoneMsg">点击这里更新您的时区设置</a></span>。
  </span>
</script>

<script>
  if (pasystem) {
    new PASystemTimezoneChecker().checkTimezone();
  }
</script>


        <!-- START VM includeCookieNotice.vm -->
<!-- END VM includeCookieNotice.vm -->

         
        
    </body>
</html>
'''
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
from multiprocessing import Manager
import time

import requests
import re
import os



def get_urls(html):
    """
    获取当前页面中所有的超链接的列表信息
    """
    links = []
    soup = BeautifulSoup( html , "html.parser" )
    url_list = soup.find_all( 'a' )
    for link in url_list:
        links.append( link.get( 'href' ) )
    return links
aa=get_urls(html)
new=[]
for i in aa:
    if 'http' and 'pdf' in i:
        new.append(i)
print(new)

data_urls=new
def getFile(url):
    file_name = url.split('/')[-1]
    u = requests.get(url)
    # f = open(file_name, 'wb')
    # f.write(u.content)
    # f.close()
    print(u.content)

    # print ("Sucessful to download" + " " + file_name)


# root_url = 'http://course.ucas.ac.cn/access/content/group/165118/'  #下载地址中相同的部分
#
# raw_url = 'file:///E:/ZjuTH/Documents/pythonCode/pythontest.html'
#
# html = getHtml(raw_url)
# url_lst = getUrl(html)
#
# os.mkdir('pdf_download')
# os.chdir(os.path.join(os.getcwd(), 'pdf_download'))

for url in data_urls[2:]:
    getFile(url)

