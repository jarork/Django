// 外部js文件
$(function () {
    // alert("外部JS文件加载完成")
    // 测试外部数据加载
    console.log(blogData);
    console.log(faderData);

    // 使用faderData

    // 声明本地的图片路径
    var BASE_URL = "../static/images/"

    var html = '';

    // <li class="slide">
    //     <a href="#">
    //         <img src="../static/images/banner01.jpg" alt="">
    //             <span class="img_info">不用苹果电脑就不是会装逼的好程序员</span>
    //     </a>
    // </li>

    // 遍历faderData生成三个li标签拼接到字符串html中
    /*
    $.each(faderData, function(index, obj){
        // console.log(index, obj);
        html += '<li class="slide">';
        html += '<a href="#">'
        html += `<img src="${BASE_URL + obj["img_url"]}" alt="">`;
        html += `<span class="img_info">${obj["img_info"]}</span>`;
        html += '</a></li>'
        console.log(html)
    })

    // 将拼接好的字符串添加到fader_controls的前面,作为兄弟元素
    $(".fader_controls").before(html);

    // 调用jQuery.easyfader.min.js提供的函数 实现轮播功能
    $('.fader').easyFader();
    */

    // 加载页面中的博客
    /*
    <!-- 每一条博客 -->
    <div class="blogs">
        <!-- 博客标题 -->
        <h3 class="blogtitle">
            <a href="#">python语言在人工智能中的优势</a>
        </h3>
        <!-- 博客图片 -->
        <div class="blogpic">
            <a href="#">
                <img src="../static/images/a.jpg" alt="">
            </a>
        </div>
        <!-- 博客文本 -->
        <p class="blogtext">
            截至8月3日24时，据31个省（自治区、直辖市）和新疆生产建设兵团报告，现有确诊病例800例（其中重症病例36例），累计治愈出院病例79030例，累计死亡病例4634例，累计报告确诊病例84464例，现有疑似病例5例。累计追踪到密切接触者792481人，尚在医学观察的密切接触者21743人。
        </p>
        <!-- 信息列表 -->
        <ul>
            <li class="author"><a href="#">作者</a></li>
            <li class="category"><a href="#">文章分类</a></li>
            <li class="pdate"><a href="#">2020-7-11</a></li>
            <li class="view"><a href="#">171</a></li>
            <li class="like"><a href="#">8</a></li>
        </ul>
    </div>
    */
    
    // 当页面加载时 显示前3条内容
    // 每次滚动时如果滚动条快要到底了再加载5条内容, 直到没有数据为止
    /*
    function load_blogs(blogData){
        var html = '';
        $.each(blogData, function(index, obj){
            var blog = `
            <div class="blogs">
                <!-- 博客标题 -->
                <h3 class="blogtitle">
                    <a href="#">${obj.blogtitle}</a>
                </h3>
                <!-- 博客图片 -->
                <div class="blogpic">
                    <a href="#">
                        <img src="../static/images/${obj.blogpic}" alt="">
                    </a>
                </div>
                <!-- 博客文本 -->
                <p class="blogtext">
                    ${obj.blogtext}
                </p>
                <!-- 信息列表 -->
                <ul>
                    <li class="author"><a href="#">${obj.bloginfo.author}</a></li>
                    <li class="category"><a href="#">${obj.bloginfo.lmname}</a></li>
                    <li class="pdate"><a href="#">${obj.bloginfo.timer}</a></li>
                    <li class="view"><a href="#">${obj.bloginfo.view}</a></li>
                    <li class="like"><a href="#">${obj.bloginfo.like}</a></li>
                </ul>
            </div>`;
            html += blog;
        })

        console.log(html)
        // 将拼接好的字符串追加到页面
        $(".blogsbox").append(html);
    }

    
    // $.each(blogData, function(index, obj){
    // console.log(index, obj);

    load_blogs(blogData.slice(0,3));

    var canLoad = true;     // 判断能否继续加载数据

    $(document).scroll(function(){
        // alert("滚了!")
        var scrollTop = $(document).scrollTop()
        var windowHeight = $(window).height()
        var documentHeight = $(document).height()
        if(documentHeight - scrollTop-windowHeight <= 200)
        {
            console.log("快到底了")
            // 获取后面 5 条数据
            // 页面中如果有3条数据,取slice(3,8)
            // 如果页面中有n条数据,取slice(n,n+5)

            // 获取一共有多少条博客
            // .blogs表示一条博客,所以可以通过获取blogs的数量得知当前页面有几个博客
            var size = $(".blogs").length;
            if (canLoad){
                var data = blogData.slice(size, size+5);
                if (data.length>0){
                    load_blogs(data);
                }
                else{
                    console.log("没数据了")
                    canLoad = false;        // 没数据了就禁止加载
                }
            }
        }
    })
    */
})