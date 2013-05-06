var doSave = $("#doSave");

function addcategory(){
	$.ajax({
		type:'POST',
		url:'/topic/reply',
		dataType:'json',
		data:$("#reply").serialize(),
		success:function(data){
			if (data.code == 200){
				$("#content").val();
				window.location.reload();
			}else{
				alert(data.code);
			}
		}
	})
}

doSave.click(function(){
	addcategory();
})