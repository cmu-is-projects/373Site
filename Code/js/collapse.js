
function toggleChevron(e) {
	$(e.target)
		.prev('#filterHeader')
		.find("i.indicator")
		.toggleClass('fa-caret-down fa-caret-right');
	}
	$('.sidebar').on('hidden.bs.collapse', toggleChevron);
	$('.sidebar').on('shown.bs.collapse', toggleChevron);
}