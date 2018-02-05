

$('#searchBar').keyup(function(){
	searchFilter($(this).val());
});

function searchFilter(input){
	var projects = $(".project");
	var matching = $('[id *= "' + input.toLowerCase() + '"]');
	if( input != "" ){
		projects.hide();
		projects.filter( matching ).show();
	}
	else{
		projects.show();
	}
}

function filterSelection( type ){
	var projects2 = $(".project");
	var allFilter = $("#allToggle");
	var webFilter = $("#webToggle");
	var mobileFilter = $("#mobileToggle");
	if(type=="web"){
		allFilter.removeClass("active");
		mobileFilter.removeClass("active");
		webFilter.addClass("active");
		projects2.hide();
		$("div[project-type*='Web']").show();
	}
	else if(type=="mobile"){
		allFilter.removeClass("active");
		mobileFilter.addClass("active");
		webFilter.removeClass("active");
		projects2.hide();
		$("div[project-type*='Mobile']").show();
	}
	else{
		allFilter.addClass("active");
		mobileFilter.removeClass("active");
		webFilter.removeClass("active");
		projects2.show();
	}

}