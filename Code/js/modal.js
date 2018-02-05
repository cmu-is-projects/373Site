

$('#searchBar').keyup(function(){
	searchFilter($(this).val());
});

function searchFilter(input){
	var projects = $(".project");
	if( input != "" ){
		projects.hide();
		$('[id *= "' + input.toLowerCase() + '"]').show();
	}
	else{
		projects.show();
	}
}

function filterSelection( type ){
	var projects = $(".project")
	if(type=="web"){
		projects.hide();
		$("div[project-type*='Web']").show();
	}
	else if(type=="mobile"){
		projects.hide();
		$("div[project-type*='Mobile']").show();
	}
	else{
		projects.show();
	}

}