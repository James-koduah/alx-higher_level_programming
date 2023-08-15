$(document).ready(function(){
	$('INPUT#btn_translate').click(()=>{
		let lang = $('INPUT#language_code').val()
		$.get( "https://hellosalut.stefanbohacek.dev/?lang="+lang, function(data){
			$("DIV#hello").text(data['hello'])
		})
	})
	$('INPUT#language_code').on("keydown", (e)=>{
		if (e.which !== 13){return}
		let lang = $('INPUT#language_code').val()
		$.get( "https://hellosalut.stefanbohacek.dev/?lang="+lang, function(data){
			$("DIV#hello").text(data['hello'])
		})
	})
})
