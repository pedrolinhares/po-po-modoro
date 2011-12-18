function update_task(input, previous_text) {
	var input = $(input);
	var text = input.val();
	var parent = input.parent();
	
	//requisicao ajax
	var id = parent.parent().attr("id");
	var url = '/task/' + id + '/';
	var field = parent.attr("class");
	$.get(url, { field: field, value: text })
		.success(function(){
			parent.text(text);
		})
		.error(function(){
			parent.text(previous_text);
			alert("error while trying to update task.");
		});

	input.remove();
	parent.click(add_input);
}

function create_task(input) {
	var parent = $(input).parent();

	var url = '/new_task/';
	var field = parent.attr("class");
	var text = $(input).val();
	var worksheet = $('table').attr("id");

	$.get(url, { field: field, value: text, worksheet: worksheet },
		function(data) {
			var new_task = data[0];
			if (field == 'title') {
				parent.text(new_task.fields['title'])	
				$('td.pomodoros', parent.parent()).text(
						new_task.fields['pomodoros']);
			}
			else {
				parent.text(new_task.fields['pomodoros'])
				$('td.title', parent.parent()).text(
						new_task.fields['title']);
			}
			parent.parent().attr("id", new_task.pk);

			//add empty line at the end
			$('#' + worksheet + ' tr:last')
			.after('<tr id="-1"><td class="title"></td><td class="pomodoros"></td></tr>');
			$('td', 'tr#-1').click(add_input);
		})
		.error(function() { alert("error while trying to update task."); });
	
	$(input).remove();
	parent.click(add_input);
}

function add_input() {
	var text = this.textContent;
	this.innerHTML = '<input type="text" value="'+ text + '" />';
	var input = $('input', $(this));
	input.focus();

	var id = $(this).parent().attr("id");
	input.keypress(function(event){
		if ((event.which == 13) && (id != -1)) {
			update_task(this, text);
		} 
		else if (event.which == 13) {
			create_task(this);
		}
	});

	input.blur(function() {
		td = $(this).parent();
		$(this).remove();
		td.text(text);
		td.click(add_input);
	});
	$(this).unbind('click');
};


$(function () {
	if ($('#inventory').length > 0) {
		$('#inventory td').click(add_input);
	}

	if ($('#todo').length > 0) {
		$('#todo td').click(add_input);
	}
});