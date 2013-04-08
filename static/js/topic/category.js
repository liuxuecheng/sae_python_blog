var doSave = $("#doSave");

function addcategory(){
	$.ajax({
		type:'POST',
		url:'/admin/addcategory',
		dataType:'json',
		data:$("categoryForm").serialize(),
		success:function(data){
			alert(data.code);
		}
	})
}

doSave.click(function(){
	addcategory()
})