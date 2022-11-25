//五种方法
//POST数据，是在报文当中的，因此请使用 setRequestHeader() 来添加 HTTP 头
// 绑定html文件上
// 绑定按钮，并且给按钮创建点击事件
function FiveMethods() {
    var n = document.getElementById("text1");
    $.ajax({
        url: 'http://localhost:5000/api/fiveMethodsShow',
        data: JSON.stringify({ n: n.value }),//数据也需要转为JSON格式。
        contentType: 'application/json',//指定字符编码格式
        type: 'POST',//发送类型
        dataType: 'json',//响应数据类型
        async: false,
        headers: {
            name: "ajax"
        },
        success: function (result) {//成功的回调
            var obj = result;
            var chart = Highcharts.chart('container', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: '五种方法结果显示'
                },

                xAxis: {
                    categories: [
                        '迭代<br>基本操作：加法<br>空间效率：线性', '迭代改进<br>加法<br>常数', '递归<br>加法<br>常数', '矩阵<br>乘法<br>常数', '近似公式<br>乘法<br>常数'
                    ],
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: '结果'
                    }
                },
                tooltip: {
                    // head + 每个 point + footer 拼接成完整的 table
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        borderWidth: 0
                    }
                },
                series: [{
                    name: '时间',
                    data: [obj.data.nameArr[0].time, obj.data.nameArr[1].time, obj.data.nameArr[2].time, obj.data.nameArr[3].time, obj.data.nameArr[4].time]
                }, {
                    name: '操作次数',
                    data: [obj.data.nameArr[0].optNum, obj.data.nameArr[1].optNum, obj.data.nameArr[2].optNum, obj.data.nameArr[3].optNum, obj.data.nameArr[4].optNum]
                }, {
                    name: '结果',
                    data: [obj.data.nameArr[0].resVal, obj.data.nameArr[1].resVal, obj.data.nameArr[2].resVal, obj.data.nameArr[3].resVal, obj.data.nameArr[4].resVal]
                }]
            });

        },
        error: function () {//失败的回调
            //不论是超时还是出错
            console.log("出错");
        }
    })
}


//迭代法计算最大
var Iterative_Max;   //位置
var Iterative_time;
function IterativeMethod_1() {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/api/iterativeEnvMax",
        contentType: 'application/json',//指定字符编码格式
        dataType: 'json',//响应数据类型
        async: false,
        success: function (result) {
            var obj = result;
            document.getElementById("form1").innerHTML = obj.data.index;
            Iterative_Max = obj.data.index;
            Iterative_time = obj.data.time;
        },
        error: function () {
            alert("错误内容");
        }
    });
    alert(Iterative_Max)
    console.log(window)
}
function IterativeMethod_2() {
    document.getElementById("form2").innerHTML = Iterative_time;
}

//递归法计算最大值
var Recursive_time;
function RecursiveEnvMax_1() {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/api/recursiveEnvMax",
        contentType: 'application/json',//指定字符编码格式
        dataType: 'json',//响应数据类型
        async: false,
        success: function (result) {
            var obj = result;
            document.getElementById("form1").innerHTML = obj.data.index;
            Recursive_time = obj.data.time;
        },
        error: function () {
            alert("错误内容");
        }
    });
}
function RecursiveEnvMax_2() {
    document.getElementById("form2").innerHTML = Recursive_time;
}
//一分钟计算
var OneMinute_time;
function OneMinuteRecursive_1() {
    IterativeMethod_1();
    console.log(window)
    // var obj = JSON.parse('{"name":"runoob","alexa":10000,"data": {"finish":1,"time":"m.runoob.com","site3":"c.runoob.com"} }');
    $.ajax({
        url: 'http://localhost:5000/api/oneMinuteRecursive',
        type: 'POST',//发送类型
        data: JSON.stringify({ n: Iterative_Max }),//数据也需要转为JSON格式。
        contentType: 'application/json',//指定字符编码格式
        dataType: 'json',//响应数据类型
        async: false,
        headers: {
            name: "ajax"
        },
        success: function (data) {//成功的回调
            var obj = data;
            if (obj.data.finish == 0) {
                document.getElementById("form1").innerHTML = "是";
            } else { document.getElementById("form1").innerHTML = "否"; }
            OneMinute_time = obj.data.time;
        },
        error: function () {//失败的回调
            //不论是超时还是出错
            console.log("出错");
        }
    })
}
function OneMinuteRecursive_2() {
    document.getElementById("form2").innerHTML = OneMinute_time;
}

var thirty_time1, thirty_time2;
function RecursiveIterationThirty_1() {
    $.ajax({
        type:"GET",
        url:"http://localhost:5000/api/recursiveIterationThirty",
        contentType:'application/json',//指定字符编码格式
        dataType:'json',//响应数据类型
        async:true,
        success:function (result) {
            var obj = result;
            document.getElementById("t1").innerHTML = obj.data.nameArr[0].index;
            thirty_time1 = obj.data.nameArr[0].time;
        },
        error:function () {
            alert("错误内容");
        }
    })
    $.ajax({
        type:"GET",
        url:"http://localhost:5000/api/recursiveIterationThirty2",
        contentType:'application/json',//指定字符编码格式
        dataType:'json',//响应数据类型
        async:true,
        success:function (result) {
            var obj = result;
            document.getElementById("t3").innerHTML = obj.data.nameArr[1].index;
            thirty_time2 = obj.data.nameArr[1].time;
        },
        error:function () {
            alert("错误内容");
        }
    })
}

function RecursiveIterationThirty_2() {
    document.getElementById("t2").innerHTML = thirty_time1;
    document.getElementById("t4").innerHTML = thirty_time2;
}

//Error
function Formula() {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/api/formula",
        contentType: 'application/json',//指定字符编码格式
        dataType: 'json',//响应数据类型
        async: false,
        success: function (result) {
            var obj = result;
            document.getElementById("form1").innerHTML = obj.data.num;
        },
        error: function () {
            alert("错误内容");
        }
    });
}
