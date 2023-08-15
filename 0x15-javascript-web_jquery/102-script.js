$(document).ready(function(){
	$('INPUT#btn_translate').click(()=>{
		let lang = $('INPUT#language_code').val()
		$.get( "https://hellosalut.stefanbohacek.dev/?lang="+lang, function(data){
			$("DIV#hello").text(data['hello'])
		})
	})
})
