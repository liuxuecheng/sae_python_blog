var doSave = $("#doSave");

function addcategory(){
	alert('error');
	$.ajax({
		type:'POST',
		url:'/topic/reply',
		dataType:'json',
		data:$("#reply").serialize(),
		success:function(data){
			if (data.code == 200){
				window.location.reload() 
			}else{
				alert(data.code);
			}
		}
	})
}

doSave.click(function(){
	addcategory()
})