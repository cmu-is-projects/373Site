

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
		var sections = document.getElementsByTagName ('section');
		if(type=="web"){
			showMobileHeaders()
			allFilter.removeClass("active");
			mobileFilter.removeClass("active");
			webFilter.addClass("active");
			projects2.hide();
			$("div[project-type='Web']").show();
			
		}
		else if(type=="mobile"){
			showMobileHeaders()
			allFilter.removeClass("active");
			mobileFilter.addClass("active");
			webFilter.removeClass("active");
			projects2.hide();
			$("div[project-type='Mobile']").show();
			hideMobileHeaders();

		}
		else{
			showMobileHeaders()
			allFilter.addClass("active");
			mobileFilter.removeClass("active");
			webFilter.removeClass("active");
			projects2.show();
		}

	}

	// Give all h1 with no mobile project id="no-mobile"
	function hideMobileHeaders(){
		$(".no-mobile").hide();
	}

	function showMobileHeaders(){
		$(".no-mobile").show();
	}





