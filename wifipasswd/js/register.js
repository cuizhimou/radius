$(function(){

	
	var error_email = false;

//失去焦点时判断邮箱

	$('#email').blur(function() {
		check_email();
	});

//判断邮箱是否合法

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@cogo.club$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
		}

	}

//发送数据请求
function query_api(datas){
	$.ajax({
		url : "/api/index",
		type : "POST",
		contentType : "application/json",
		data : datas,
		success : function (data) {

			//发送成功
			if ("1000"==data.code){

				$('#reg_form').next().html('wifi账号和密码已经发送到您的邮箱请查收')
				$('#reg_form').next().show();

			}
			//发送异常请重试
			if ("3000"==data.code){
				$('#reg_form').next().html('邮件发送异常请重试！')
				$('#reg_form').next().show();
			}
			//邮箱不合法
			if ("2000"==data.code){
				$('#reg_form').next().html('邮箱不合法！')
				$('#reg_form').next().show();
			}


		}

	})
}



//提交表单
//	$('#reg_form').submit(function()s

function send(){
		
		alert("test")
		check_email();

		if(error_email == false)
		{
			mydata={'umail' : $('#email').val()}
			query_api(JSON.stringfy(mydata))
			return true;
		}
		else
		{
			$('#reg_form').next().html('请确认输入的邮箱！')
			$('#reg_form').next().show();
			return false;
		}

	}

})