var doSave = $("#doSave");

function addcategory(){
	$.ajax({
		type:'POST',
		url:'/admin/topic/addcategory',
		dataType:'json',
		data:$("#categoryForm").serialize(),
		success:function(data){
			if (data.code == 200){
				$('#categoryModal').modal('hide');
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