var level=Array(4);level[1]="Alto";
level[2]="Medio";level[3]="Bajo";
var months=Array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");var object;$(document).ready(function(){function createArrowUp(){if($(document).scrollTop()>250){if($("#goTop").length==0)
{$("body").append("<div id='goTop' title='Subir'></div>");$("#goTop").click(function(){$('html,body').animate({scrollTop:0},{duration:"slow"})});}
$("#goTop").fadeIn();}else{$("#goTop").fadeOut();}if($("html").width()>1100){$("#goTop").css("right",(Math.floor(($("html").width()-1000)/2)-30));}else{$("#goTop").css("right",20);}}
createArrowUp();$(document).scroll(function(){createArrowUp();});
$(window).resize(function(){createArrowUp();});

$(".form_block .jobLanguage .add span").click(function(){var languageId=$("#language").val();var talk=$("input:radio[name=talk]:checked").val();var written=$("input:radio[name=written]:checked").val();if(languageId>0 && talk!=undefined && written!=undefined){var languageText=$("#language option:selected").text();if($("#lang_"+languageId).length==0){var content="<div class='lang_selected' id='lang_"+languageId+"'>";content+="<div class='language bold'>"+languageText+"</div>";content+="<div class='info'>Hablado:</div><div class='talkwritten bold'>"+level[talk]+"</div>";content+="<div class='info'>Escrito:</div><div class='talkwritten bold'>"+level[written]+"</div>";content+="<div class='remove'><span class='button' onclick=\"languageRemoveList("+languageId+");\">Quitar</span></div>";content+="<input type='hidden' name='lang_t_"+languageId+"' value='"+talk+"'>";content+="<input type='hidden' name='lang_w_"+languageId+"' value='"+written+"'>";content+="</div>";
$("#jobLanguageList").append(content);}}});$("#headerLogin .btnLogin").click(function(){$("#login").slideDown();$("#loginMail").focus();});$("#loginForm>div .img").click(function(){$("#login").slideUp();});
$("#loginBtn").click(function(){if(validateForm_programmersLogin()){$("#loginForm").submit();}});$("#menuSmarth").click(function(){if($("nav ul").is(":visible")){$("nav ul").slideUp("slow");}else{$("nav ul").slideDown("slow");}});$("#cookie").click(".btnOption",function(){console.log("LLL");$(this).slideUp();});});

function languageRemoveList(languageId){$("#lang_"+languageId).remove();}

function displayLayer(layerName,visible){if(visible)
document.getElementById(layerName).style.display='inline';else
document.getElementById(layerName).style.display='none';}

function showHide_layer(idLayer){if(document.getElementById("sh_div"+idLayer))
{if(document.getElementById("sh_div"+idLayer).style.display=='none' || document.getElementById("sh_div"+idLayer).style.display==''){$("#sh_div"+idLayer).slideDown();if(document.getElementById("sh_img"+idLayer))
$("#sh_img"+idLayer).attr("src","/img/showHide_hide.png");}else{$("#sh_div"+idLayer).slideUp();if(document.getElementById("sh_img"+idLayer))
$("#sh_img"+idLayer).attr("src","/img/showHide_show.png");}}}

function secondsToHours(Seconds){if(Seconds>0)
{var Days=Math.floor(Seconds / 86400);Seconds-=Days * 86400;var Hours=Math.floor(Seconds / 3600);Seconds-=Hours * (3600);var Minutes=Math.floor(Seconds / 60);Seconds-=Minutes * (60);var TimeStr = ((Days > 0) ? Days + " dias " : "") + LeadingZero(Hours) + ":" + LeadingZero(Minutes) + ":" + LeadingZero(Seconds);if(Days>0 || Hours>0 || Minutes>0 || Seconds>0){return TimeStr;}}
return "00:00:00";}

function LeadingZero(Time){return (Time < 10) ? "0" + Time : + Time;}

function isIE(){var myNav=navigator.userAgent.toLowerCase();return (myNav.indexOf('msie')!=-1) ? parseInt(myNav.split('msie')[1]) : false;}

function layerShowClock(){var posTop=(($(window).height()/2)-(8) - 40);var posLeft=(($(window).width()/2)-(8));$("#layerClock").attr("style", "top:"+posTop+"px;left:"+posLeft+"px;").show();
$("#layer").fadeIn();}

function layerShow(){var posTop=(($(window).height()/2)-($('#layerc').height()/2) - 40);var posLeft=(($(window).width()/2)-($('#layerc').width()/2));if(posTop<10){posTop=10;}
$('#layerc').css({"top":posTop, "left":posLeft});$('#layerc').fadeIn();
$("#layerClock").hide();}

function layerClose(){slideImages.close();$('#layer').fadeOut('slow');}

function goToId(idName){if($("#"+idName).length){var target_offset = $("#"+idName).offset();var target_top=target_offset.top;$('html,body').animate({scrollTop:target_top},{duration:"slow"});}}

function setCookie(nombre,valor,caducidad){var expireDate=new Date();expireDate.setTime(expireDate.getTime()+(caducidad*24*60*60*1000));
document.cookie=nombre + "=" + encodeURIComponent(valor) + ";expires=" + expireDate.toGMTString() + ";path=/";}

function getCookie(nombre){if(document.cookie.length>0){start=document.cookie.indexOf(nombre + "=");if(start!=-1){start=start + nombre.length+1;end=document.cookie.indexOf(";",start);if(end==-1)
end=document.cookie.length;return unescape(document.cookie.substring(start,end));}}
return "";}
function validateForm_comment(rating,comment,stars,idanswer){if(idanswer){var formId="formComment_"+idanswer;}else{var formId="formComment";}
var nombre=document.forms[formId].nombre.value;var id_enombre=document.forms[formId].getElementsByClassName("enombre")[0];var correo=document.forms[formId].correo.value;var id_ecorreo=document.forms[formId].getElementsByClassName("ecorreo")[0];if(rating){var id_evaloracion=document.forms[formId].getElementsByClassName("evaloracion")[0];if(stars){var stars=document.forms[formId].stars.value;return_radio=validate_select(stars,id_evaloracion,"Determina tu valoración")}else{var radio=document.forms[formId].valoracion;return_radio=validate_radio(formId,"valoracion",id_evaloracion,"Determina si tu valoración en positiva o negativa");}}else{return_radio=1;}if(comment){var comentario=document.forms[formId].comentario.value;var id_ecomentario=document.forms[formId].getElementsByClassName("ecomentario")[0];return_comentario=validate_text(comentario,id_ecomentario,"Indica un comentario");}else{return_comentario=1;}
var return_nombre=validate_text(nombre,id_enombre,"Indica un nombre valido");var return_mail=validate_email(correo,id_ecorreo,1);if(return_nombre==1 && return_mail==1 && return_radio==1 && return_comentario){disableButtonSend();return true;}
return false;}

function validateForm_recommend(){var nombre=document.formRecommend.nombre.value;var id_enombre=document.getElementById("enombre");var correo=document.formRecommend.correo.value;var id_ecorreo=document.getElementById("ecorreo");var nombred=document.formRecommend.nombred.value;var id_enombred=document.getElementById("enombred");var correod=document.formRecommend.correod.value;var id_ecorreod=document.getElementById("ecorreod");var return_nombre=validate_text(nombre,id_enombre,"Indica un nombre valido");var return_mail=validate_email(correo,id_ecorreo,1);var return_nombred=validate_text(nombred,id_enombred,"Indica un nombre valido");var return_maild=validate_email(correod,id_ecorreod,1);if(return_nombre==1 && return_mail==1 && return_nombred==1 && return_maild==1){disableButtonSend();return true;}
return false;}

function validateForm_participacion(){var return_mail=validate_email(trim(document.formRecommend.correo.value),document.getElementById("ecorreo"),1);if(return_mail==1){disableButtonSend();return true;}
return false;}

function validateForm_foro(id){if(document.forms["formUpd_"+id]){var formId="formUpd_"+id;}else{var formId="form_"+id;}
var nombre=document.forms[formId].nombre.value;var id_enombre=document.getElementById("enombre_"+id);var correo=document.forms[formId].correo.value;var id_ecorreo=document.getElementById("ecorreo_"+id);var titulo=document.forms[formId].titulo.value;var id_etitulo=document.getElementById("etitulo_"+id);var texto=document.forms[formId].texto.value;var id_etexto=document.getElementById("etexto_"+id);var return_nombre=validate_text(nombre,id_enombre,"Indica un nombre válido");var return_mail=validate_email(correo,id_ecorreo,1);var return_titulo=validate_text(titulo,id_etitulo,"Indica un título para la nota");var return_texto=validate_text(texto,id_etexto,"El campo texto ha de contener como mínimo 10 carácteres",10);var return_textMax=1;if(return_texto==1){return_textMax=validate_maxLenght(texto,id_etexto,"El campo texto ha de contener como máximo 15.000 carácteres",15000);}if(return_nombre==1 && return_mail==1 && return_titulo==1 && return_texto==1 && return_textMax==1){disableButtonSend("idSend_"+id);return true;}
return false;}

function validateForm_tablon(){var nombre=$("#nombre").val();var id_enombre=document.getElementById("enombre");var correo=$("#correo").val();var id_ecorreo=document.getElementById("ecorreo");var titulo=$("#titulo").val();var id_etitulo=document.getElementById("etitulo");var dateEnd=$("#dateend").val();var id_edateEnd=document.getElementById("edateend");var texto=$("#texto").val();var id_etexto=document.getElementById("etexto");var return_nombre=validate_text(nombre,id_enombre,"Indica un nombre válido");var return_mail=validate_email(correo,id_ecorreo,1);var return_titulo=validate_text(titulo,id_etitulo,"Indica un título para la nota");var return_isdate=validate_dateInOneYear(dateEnd,id_edateEnd);var return_texto=validate_text(texto,id_etexto,"El campo texto ha de contener como mínimo 10 carácteres",10);var return_textMax=1;if(return_texto==1){return_textMax=validate_maxLenght(texto,id_etexto,"El campo texto ha de contener como máximo 15.000 carácteres",15000);}if(return_nombre==1 && return_mail==1 && return_titulo==1 && return_texto==1 && return_isdate==1 && return_textMax==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_job(){var name=$("#name").val();var id_ename=document.getElementById("ename");var mail=$("#mail").val();var id_email=document.getElementById("email");var dateEnd=$("#dateend").val();var id_edateEnd=document.getElementById("edateend");var country=$("#country").val();var id_ecountry=document.getElementById("ecountry");var title=$("#title").val();var id_etitle=document.getElementById("etitle");var description=$("#description").val();var id_edescription=document.getElementById("edescription");var return_name=validate_text(name,id_ename,"Indica un nombre válido");var return_mail=validate_email(mail,id_email,1);var return_isdate=validate_dateInOneYear(dateEnd,id_edateEnd);var return_country=validate_select(country,id_ecountry,"Selecciona un país");var return_titulo=validate_text(title,id_etitle,"Indica un título para la oferta");var return_description=validate_text(description,id_edescription,"La descripción de la oferta ha de contener como mínimo 10 carácteres",10);if(return_name==1 && return_mail==1 && return_isdate==1 && return_country==1 && return_titulo==1 && return_description==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_dicccionario(){var name=$("#name").val();var id_ename=document.getElementById("ename");var mail=$("#mail").val();var id_email=document.getElementById("email");var word=$("#word").val();var id_eword=document.getElementById("eword");var description=$("#description").val();var id_edescription=document.getElementById("edescription");var return_name=validate_text(name,id_ename,"Indica un nombre válido");var return_mail=validate_email(mail,id_email,1);var return_word=validate_text(word,id_eword,"Indica una palabra para el diccionario");var return_description=validate_text(description,id_edescription,"La descripción de la palabra tiene que contener como mínimo 3 carácteres",3);if(return_name==1 && return_mail==1 && return_word==1 && return_description==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_programmersLogin(){var mail=document.getElementById("loginMail");var password=document.getElementById("loginPas");var return_mail=validate_email(mail.value,"",1);$("#loginMail").removeClass("borderRed");
$("#loginPas").removeClass("borderRed");if(return_mail==1 && password.value.length>=6){return true;}else{if(password.value.length<6){$("#loginPas").addClass("borderRed");$("#loginPas").focus();}if(return_mail==0){$("#loginMail").addClass("borderRed");$("#loginMail").focus();}}
return false;}

function validateForm_programmersValidate(){var mail=$("#m").val();var email=document.getElementById("em");var password=$("#p").val();var epassword=document.getElementById("ep");var return_mail=validate_email(mail,email,1);var return_pass=validate_text(password,epassword,"La contraseña tiene que tener 6 caracteres o mas",6);if(return_mail==1 && return_pass==1){return true;}
return false;}

function validate_password(pass1,pass2,id_eobj){if(pass1==pass2 && pass1.length>=6){return_password=1;id_eobj.innerHTML="";
id_eobj.style.display="none";return 1;}else{if(pass1.length<6)
id_eobj.innerHTML="La contraseña tiene que tener un mínimo de 6 caracteres";else
id_eobj.innerHTML="La copia de la contraseña no coincide";id_eobj.style.display="block";
return 0;}}
$(document).ready(function(){$("#sendEncuesta").click(function(){var idg=$("#encuesta form").attr("id");idg=idg.substr(1);
var idv=$("#encuesta input:radio[name=enc]:checked").val();$.post("/ajax/encuesta_vote.php", {"idg":idg, "idv":idv}, function(data){if(data.content){$("#encuesta>div:last-child").html(data.content);$("#encuestaTotal").html(data.total);}}, "json");return false;});
$("#sendRecommend").click(function(){var ver=$("form[name=formComment] input[name=ver]").val();var id=$("form[class=recommendForm2] input[name=id]").val();var name=$("form[class=recommendForm2] input[name=name]").val();var mail=$("form[class=recommendForm2] input[name=mail]").val();var url="";var title="";if($("form[class=recommendForm2] input[name=url]").length)
url=$("form[class=recommendForm2] input[name=url]").val();if($("form[class=recommendForm2] input[name=title]").length)
title=$("form[class=recommendForm2] input[name=title]").val();if(name.length>0 && validate_email(mail, "", 1)){$("#sendRecommend").hide();$("#sendRecommend").parent().addClass("clockWithImg16");
$.post("/ajax/recommend.php",
{"id":id, "ver":ver, "name":name, "mail":mail, "url":url, "title":title},
function(data){if(data.send==1){$("form[class=recommendForm2] input[name=mail]").val("");if(data.text){$("form[class=recommendForm2] p:first").addClass("f_black").html(data.text);}}
$("#sendRecommend").parent().removeClass("clockWithImg16");$("#sendRecommend").show();},"json"
);}else{$("form[class=recommendForm2] p:first").removeClass("f_black").html("El nombre y el correo son obligatorios");}});});

function validateFormAjax(filePHP,idForm){$("#"+idForm+" .errorForm").remove();$.post(filePHP, $("#"+idForm).serialize(),function(data){if(data.result=="1"){$("#"+idForm)[0].reset();if(data.hide)
$("#"+idForm).hide(500);if(data.url)
window.location.href=data.url;else
$(".message").addClass("ok").html(data.message).fadeIn();}else{form_showErrors(data.errors);}}, "json");return false;}

function form_showErrors(arrayErrors){for(key in arrayErrors)
{if($("#"+key).length){var value=arrayErrors[key];if(value){$("#"+key).before("<div class='errorForm'>"+value+"</div>");}}}}
var Conexion=false;var js_idReloj="";var js_cadena="";var js_valueCadena="";var js_display="inline";var js_functionExecute="";function Conectar(){if(window.XMLHttpRequest)
Conexion=new XMLHttpRequest();else if(window.ActiveXObject)
Conexion=new ActiveXObject("Microsoft.XMLHTTP");}
function ContenidoHTML(idContenido){if(Conexion.readyState!=4) return;if(Conexion.status==200){if(js_functionExecute)
eval(js_functionExecute)(idContenido);}else{document.getElementById(idContenido).innerHTML=Conexion.status+"-"+Conexion.statusText;}if(document.getElementById(js_idReloj)){document.getElementById(js_idReloj).style.visibility="hidden";document.getElementById(js_idReloj).style.display="none";}
Conexion=false;}

function modifyContentHTML(idContenido){if(Conexion.responseText){document.getElementById(idContenido).style.display=js_display;document.getElementById(idContenido).innerHTML=Conexion.responseText;}else{document.getElementById(idContenido).style.display=js_display;document.getElementById(idContenido).innerHTML="";}}
function SolicitudHTML(idContenido,Cadena,filePHP){if(Cadena && Cadena!=js_cadena){if(Conexion) return;Conectar();if(Conexion){if(document.getElementById(js_idReloj))
{document.getElementById(js_idReloj).style.visibility="visible";document.getElementById(js_idReloj).style.display="inline";}
js_cadena=Cadena;Conexion.open("POST",filePHP,true);
Conexion.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");Conexion.onreadystatechange=function(){ContenidoHTML(idContenido);}
date=new Date();Conexion.send("idContenido="+idContenido+"&word="+Cadena+"&"+date.getTime());}else
document.getElementById(idContenido).innerHTML="ERROR JS : No connected";}}

function returnHTML(idContenido,idReloj,filePHP,Cadena,functionExecute){js_idReloj=idReloj;js_valueCadena=Cadena;
js_cadena='';if(functionExecute=="" || functionExecute==undefined)
js_functionExecute="modifyContentHTML";else
js_functionExecute=functionExecute;if(Conexion!=false){Conexion=false;if(document.getElementById(js_idReloj))
{document.getElementById(js_idReloj).style.visibility="hidden";document.getElementById(js_idReloj).style.display="none";}}
SolicitudHTML(idContenido,Cadena,filePHP);}
var textSelected;$(document).ready(function(){$(document).keyup(function(event){if(event.which==27){closePreview();layerClose();}});editor_viewImages();});function editor_viewImages(){$("img.editor_img").click(function(){var id=$(this).parents(".ce").attr("id");var srcImage=$(this).attr("src");slideImages.clear();
slideImages.firstImage=srcImage;$("#"+id+" img.editor_img").each(function(){if($(this).attr("data-url")){slideImages.addImageAndLink($(this).attr("src"), $(this).attr("data-url"));}else{slideImages.addImage($(this).attr("src"));}});slideImages.showLayers();});}

function editor_selectFiles(name){$("#files"+name).click();}

function editor_uploadFilesChange(name){if($("#files"+name).val())
editor_uploadFiles(name);}

function editor_selectImages(name){$("#images"+name).click();}

function editor_uploadImagesChange(name){if($("#images"+name).val())
editor_uploadImages(name);}

function editor_uploadImages(name){$("#upi"+name+">div:nth-child(2)").removeClass("message_arrow_wrapper message_arrow_lt f_red").addClass("text").html('').addClass("clockWithImg16");var idImagenes=document.getElementById("images"+name);var archivos=idImagenes.files;var data=new FormData();for(var i=0;i<archivos.length;i++){data.append("archivo"+i,archivos[i]);}
$.ajax({url:"/ajax/ajax_editor_uploadImages.php",
type:"POST",
data:data,
dataType:"json",
contentType:false,
processData:false,
cache:false}).done(function(data){$("#upi"+name+">div:nth-child(2)").removeClass("clockWithImg16");if(data.img){$("#img"+name).append(data.img);$("#upi"+name+">div:nth-child(2)").html(data.msg);
createEventClickThumbnail(name);var textarea=$("#"+name).val();$.each(data.name, function(index,value){textarea+="\n[img]/usr/tmp/"+value+"[/img]";});
$("#"+name).val("").val(textarea);setCursorAtEnd(name);}else{$("#upi"+name+">div:nth-child(2)").addClass("f_red").html(data.err);}});return false;}

function createEventClickThumbnail(name){$("#img"+name+" .editor_img_th .th_add").unbind("click").click(function(){insTag("[img]","[/img]",name,"/usr/tmp/"+$(this).parent().parent().parent().attr("id"),true);});
$("#img"+name+" .editor_img_th .th_rm").unbind("click").click(function(){var url=prepareStringToRegExp($(this).parent().parent().parent().attr("id"));$(this).parent().parent().parent().parent().hide();
var re=new RegExp("\\[img\\]/usr/tmp/"+url+"\\[/img\\]","gi");var textarea=$("#"+name).val();$("#"+name).val("").val(textarea.replace(re,''));});}

function editor_uploadFiles(name){$("#upf"+name+">div:nth-child(2)").removeClass("message_arrow_wrapper message_arrow_lt f_red").addClass("text").html('').addClass("clockWithImg16");var idImagenes=document.getElementById("files"+name);var archivos=idImagenes.files;var data=new FormData();for(var i=0;i<archivos.length;i++){data.append("archivo"+i,archivos[i]);}
$.ajax({url:"/ajax/ajax_editor_uploadFiles.php",
type:"POST",
data:data,
dataType:"json",
contentType:false,
processData:false,
cache:false}).done(function(data){$("#upf"+name+">div:nth-child(2)").removeClass("clockWithImg16");if(data.result){if($("#file"+name).html()=="")
{$("#file"+name).append("<div style='padding-top:2px;'><div class='message_arrow_wrapper message_arrow_lb' id='infoPushImg'>Estos archivos ser&aacute;n incluidos al final de tu mensaje</div></div>");}
$("#file"+name).append(data.result);$("#upf"+name+">div:nth-child(2)").html(data.msg);
createEventRemoveFile(name);}else{$("#upf"+name+">div:nth-child(2)").addClass("f_red").html(data.err);}});return false;}

function createEventRemoveFile(name){$("#file"+name+" .editor_file .img").unbind("click").click(function(){var parent=$(this).parent();$.post("/ajax/ajax_editor_deleteFile.php", {fileName:$(this).parent().attr("id")}, function(data){$("#file"+name).append(data.result);parent.remove();},"json");});}
function closePreview(){$('#layerPreview').hide();$('#layerPreviewIntern').hide();
$('#layerHelp').hide();$('#layerHelpIntern').hide();
$('#editor_idclock').show();}

function insTag(tagStart,tagEnd,field,content,positionLast){var input=document.getElementById(field);if(positionLast==undefined)
positionLast=false;if(typeof document.selection != 'undefined' && document.selection){input.focus();var sel=document.selection.createRange();if(content){var insText=content}else{if(sel.text){var insText=sel.text;}else if(typeof(textSelected)=='object'){var insText=textSelected.text;}else if(tagEnd){var insText="Reemplace este texto";}else{var insText="";}}
input.focus();if(textSelected){var sel=textSelected;}if(tagEnd){sel.text=tagStart+insText+tagEnd;}else{sel.text=tagStart+insText;}
sel.select();}else if(typeof input.selectionStart != 'undefined'){if(!textSelected)
textSelected=input;if(typeof textSelected.scrollTop != 'undefined'){var st=textSelected.scrollTop;var sl=textSelected.scrollLeft;}
var start=textSelected.selectionStart;var end=textSelected.selectionEnd;if(content){var insText=content}else{if(start==end && tagEnd){var insText = "Reemplace este texto";}else{var insText=textSelected.value.substring(start,end);}}if(tagEnd){textSelected.value=textSelected.value.substr(0,start)+tagStart+insText+tagEnd+input.value.substr(end);}else{textSelected.value=textSelected.value.substr(0,start)+tagStart+insText+input.value.substr(end);}
textSelected.focus();if(typeof textSelected.scrollTop != 'undefined'){textSelected.scrollTop=st;textSelected.scrollLeft=sl;}if(start!=end || positionLast==true){textSelected.setSelectionRange(start+tagStart.length+insText.length+tagEnd.length, start+tagStart.length+insText.length+tagEnd.length);}else{textSelected.setSelectionRange(start+tagStart.length, start+tagStart.length+insText.length);}}else{if(tagEnd)
input.value+=' '+tagStart+'Reemplace este texto'+tagEnd;}
textSelected="";return;}
  

function putCursorAtEnd(id){var obj = $("#"+id),
val=obj.val();obj.focus().val("").val(val);
obj.scrollTop(obj[0].scrollHeight);}

function rowAdd(field){var rows=document.getElementById(field).rows;if(rows<60){document.getElementById(field).rows=rows+5;}}

function rowDel(field){var rows=document.getElementById(field).rows;if(rows>10){document.getElementById(field).rows=rows-5;}}

function showDiv(field,event,divName){if($('#youtube'+field).lenght)
document.getElementById('youtube'+field).style.display='none';document.getElementById('smile'+field).style.display='none';
$("#"+divName).css({"top":(event.pageY+5), "left":event.pageX}).show();if(divName.substr(0,4)=="yout"){$("#"+divName+" input[type=text]").focus();}
return;}

function posCursor(field){var input=document.getElementById(field);if(typeof document.selection != 'undefined' && document.selection){input.focus();textSelected=document.selection.createRange();
return;}else if(typeof input.selectionStart != 'undefined'){textSelected=input;return;}}

function previewHelp(){$('#layerHelp').attr("style", "top:0px;height:"+$(document).height()+"px; width:"+$(window).width()+"px;display:inline;");
$('#layerHelpIntern').attr("style", "top:"+$(document).scrollTop()+"px;display:inline;");}

function Solicitud(idContenido,Cadena,filePHP){if(Cadena && Cadena!=js_cadena){if(Conexion) return;Conectar();if(Conexion){if(document.getElementById(js_idReloj))
{document.getElementById(js_idReloj).style.visibility="visible";document.getElementById(js_idReloj).style.display="inline";}
js_cadena=Cadena;Conexion.open("POST",filePHP,true);
Conexion.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");Conexion.onreadystatechange=function(){ContenidoHTML(idContenido);}
date=new Date();Conexion.send("idContenido="+idContenido+"&word="+Cadena+"&"+date.getTime());}else
document.getElementById(idContenido).innerHTML="ERROR JS : No connected";}}

function editor_preview(idDestino,idReloj,filePHP,idOrigen,previewWidth){$('#layerPreview').attr("style", "top:0px;height:"+$(document).height()+"px; width:"+$(window).width()+"px;display:inline;");if(isIE()){$('#layerPreviewIntern').attr("style", "top:"+$('html, body').scrollTop()+"px;");}else{$('#layerPreviewIntern').attr("style", "top:"+$(document).scrollTop()+"px;");}
$("#layerPreviewIntern").css({"width":previewWidth, "margin-left":-parseInt(previewWidth/2), "display":"inline"});var filesList=$("#"+idOrigen).parent("form").find("input[name='file[]']");var files=new Array();filesList.each(function(){files.push($(this).val());});
$("#editor_preview").html("<div class='clock'><img src='/img/ajaxActivity.gif'></div>");$("#editor_preview").load(filePHP, {word:$("#"+idOrigen).val(), file:files});}
function show_editorUser_layer(event){$("#editorUser").addClass("block_info");$("#editorUser").css({"top":(event.pageY+10), "left":event.pageX}).fadeIn();$("#editorUser").click(function(){$("#editorUser").fadeOut()});}

function checkUrlYouTube(idLayer){var url=$("#"+idLayer+" input[type=text]").val();var youtubeCode=youtubeGetKey(url);if(youtubeCode){var id=idLayer.substr(7);$("#"+idLayer+" input[type=text]").val("");$("#"+idLayer).hide();
insTag("[youtube]http://www.youtube.com/embed/"+youtubeCode+"[/youtube]\n", "", id);}}

function youtubeKeyPress(e,idLayer){var teclaPulsada=window.event ? window.event.keyCode:e.which;if(teclaPulsada==13){checkUrlYouTube(idLayer);return false;}
return true;}
var slideImages={images:[],
imagesLink:[],
imageShowed:0,
firstImage:"",

addImage:function(image){this.images.push(image);},
addImageAndLink:function(image,imagesLink){this.images.push(image);this.imagesLink.push(imagesLink);},

addImages:function(images){if($.isArray(images)){this.images=this.images.concat(images);}},
clear:function(){this.images=[];this.imageShowed=0;},

showLayers:function(){layerShowClock();var heightScreen=$(window).height()-60;var widthScreen=$(window).width()-60;$("#layerc .layer-wrapper").height(heightScreen);$("#layerc").width(widthScreen);if(this.images.length==this.imagesLink.length){$("#layerc").html("\
<div class='layer-wrapper center'>\
<div class='slide-wrapper'>\
<a href=''><img src=''></a>\
<div class='arrow arrowLeft'></div>\
<div class='arrow arrowRight'></div>\
</div>\
<a href='' target='_blank' class='url'>casa</a>\
</div>\
<div class='button-close'>x</div>");}else{$("#layerc").html("\
<div class='layer-wrapper center'>\
<div class='slide-wrapper'>\
<img src=''>\
<div class='arrow arrowLeft'></div>\
<div class='arrow arrowRight'></div>\
</div>\
<a href='' target='_blank' class='url'>casa</a>\
</div>\
<div class='button-close'>x</div>");}
$("#layerc .slide-wrapper").css("height",(heightScreen-60)+"px");$("#layerc .slide-wrapper img").css({"max-height":(heightScreen-60)+"px", "max-width":(widthScreen-60)+"px"});this.selectFirstImage();
this.showHideArrows();this.showImage();
$(".button-close").click(function(){slideImages.clear();layerClose();});$(".slide-wrapper .arrowRight").click(function(){slideImages.showNextImage();});
$(".slide-wrapper .arrowLeft").click(function(){slideImages.showPreviousImage();});
$(window).bind("keydown",function(event){if(event.which==39){slideImages.showNextImage();event.preventDefault();
return false;}if(event.which==37){checkUrlYouTube
slideImages.showPreviousImage();event.preventDefault();
return false;}});},

close:function(){$(window).unbind("keydown");},

showNextImage:function(){if(this.imageShowed<this.images.length-1){this.imageShowed++;this.showImage();
this.showHideArrows();}},

showPreviousImage:function(){if(this.imageShowed>0){this.imageShowed--;this.showImage();
this.showHideArrows();}},

showHideArrows:function(){if(this.imageShowed<this.images.length-1){$("#layerc .slide-wrapper .arrowRight").addClass("show");}else{$("#layerc .slide-wrapper .arrowRight").removeClass("show");}if(this.imageShowed>0){$("#layerc .slide-wrapper .arrowLeft").addClass("show");}else{$("#layerc .slide-wrapper .arrowLeft").removeClass("show");}},

selectFirstImage:function(){if(this.firstImage && this.images.length>1){for(var i=0;i<this.images.length;i++)
{if(this.images[i]==this.firstImage){this.imageShowed=i;break;}}}},

showImage:function(){$("#layerc img").hide();$("#layerc .layer-wrapper .slide-wrapper").addClass("clockWithImg32");var folder=this.images[this.imageShowed].substring(0,5);if(folder=="/usr/" || folder=="/pdf/"){var url="http://www.lawebdelprogramador.com"+this.images[this.imageShowed]}else{var url=this.images[this.imageShowed];}if(this.images.length==this.imagesLink.length){var imageLink=this.imagesLink[this.imageShowed];}
$("#layerc img").unbind("error").unbind("load").removeAttr("src").attr("src", this.images[this.imageShowed]).error(function(){$("#layerc").show();layerShow();
$("#layerc img").show();$("#layerc .layer-wrapper .slide-wrapper").removeClass("clockWithImg32");}).load(function(){$("#layerc").show();layerShow();
$("#layerc .slide-wrapper a").attr("href",imageLink);$("#layerc .slide-wrapper .url").attr("href", url);$("#layerc img").show();$("#layerc .layer-wrapper .slide-wrapper").removeClass("clockWithImg32");});
$("#layerc .url").attr("href",url).text(url);},}
function validateForm_programmersAdd(){var name=document.formProgrammersAdd.name.value;var id_ename=document.getElementById("ename");var country=document.formProgrammersAdd.country.value;var id_ecountry=document.getElementById("ecountry");var mail=document.formProgrammersAdd.mail.value;var id_email=document.getElementById("email");if(document.getElementById("password")){var password=document.formProgrammersAdd.password.value;var id_epassword=document.getElementById("epassword");var password2=document.formProgrammersAdd.password2.value;var return_password=validate_password(password,password2,id_epassword);}else{var return_password=1;}
var return_nombre=validate_text(name,id_ename,"Indica un nombre v&aacute;lido");var return_country=validate_select(country,id_ecountry,"Selecciona un pa&iacute;s");var return_mail=validate_email(mail,id_email,1);if(return_nombre==1 && return_country==1 && return_mail==1 && return_password==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_programmersChangePassword(){var passwordold=document.formProgrammersAdd.passwordold.value;var id_epasswordold=document.getElementById("epasswordold");var password=document.formProgrammersAdd.password.value;var id_epassword=document.getElementById("epassword");var password2=document.formProgrammersAdd.password2.value;var return_password=validate_password(password,password2,id_epassword);if(passwordold.length<6){id_epasswordold.innerHTML="La contrase&ntilde;a tiene que tener un m&iacute;nimo de 6 caracteres";id_epasswordold.style.display="block";}else{id_epasswordold.innerHTML="";id_epasswordold.style.display="none";if(return_password==1){disableButtonSend("idSend");return true;}}
return false;}

function validateForm_programmersRemember(){var mail=document.formProgrammersAdd.mail.value;var id_email=document.getElementById("email");var return_mail=validate_email(mail,id_email,1);if(return_mail==1 ){disableButtonSend("idSend");return true;}
return false;}

function upImage_clickDiv(name){$("#"+name).click();}

function upImage(file,formId){$("#idclock").show();$("#picture").hide();
var action=$("#"+formId).attr("action");$("#"+formId).attr({"target":'iframe_null', "action":file});$("#"+formId).submit();
$("#"+formId).attr({"target":'', "action":action});}

function delImage(){$.post("delImage.php", {type:$("#typeImg").val()}, function(data){if(data=="1"){$("#picture").attr({src:"/img/anonymouse.png", width:"80", height:"80"});$("#delImage").hide();}});}

function validateForm_curriculum1(){var name=document.formProgrammersAdd.name.value;var id_ename=document.getElementById("ename");var country=document.formProgrammersAdd.country.value;var id_ecountry=document.getElementById("ecountry");var mail=document.formProgrammersAdd.mail.value;var id_email=document.getElementById("email");var birthDay=document.getElementById("datebirthday_d").value;var birthMonth=document.getElementById("datebirthday_m").value;var birthYear=document.getElementById("datebirthday_y").value;var id_ebirthday=document.getElementById("ebirthday");var webpage=document.getElementById("webpage").value;var id_ewebpage=document.getElementById("ewebpage");var return_nombre=validate_text(name,id_ename,"Indica un nombre v&aacute;lido");var return_country=validate_select(country,id_ecountry,"Selecciona un pa&iacute;s");var return_mail=validate_email(mail,id_email,1);var return_isdate=isValidDate(birthDay,birthMonth,birthYear);var return_url=validate_url(webpage,id_ewebpage,0);if(return_isdate==true){id_ebirthday.innerHTML="";id_ebirthday.style.display="none";}else{id_ebirthday.innerHTML="La fecha de nacimiento no es correcta";id_ebirthday.style.display="block";}if(return_isdate==false){$("#datebirthday_d").focus();}else if(return_url==0){$("#webpage").focus();}if(return_nombre==1 && return_mail==1 && return_country==1 && return_isdate==true && return_url==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_list(){var name=document.formProgrammersAdd.name.value;var id_ename=document.getElementById("ename");var country=document.formProgrammersAdd.country.value;var id_ecountry=document.getElementById("ecountry");var mail=document.formProgrammersAdd.mail.value;var id_email=document.getElementById("email");var webpage=document.getElementById("webpage").value;var id_ewebpage=document.getElementById("ewebpage");var return_nombre=validate_text(name,id_ename,"Indica un nombre v&aacute;lido");var return_country=validate_select(country,id_ecountry,"Selecciona un pa&iacute;s");var return_mail=validate_email(mail,id_email,1);var return_url=validate_url(webpage,id_ewebpage,0);if(return_nombre==1 && return_mail==1 && return_country==1 && return_url==1 && return_text==1){disableButtonSend("idSend");return true;}
return false;}

function validateForm_videotutorialesAdd(){var titulo=$("#titulo").val();var id_etitulo=document.getElementById("etitulo");var comentarios=$("#comentarios").val();var id_ecomentarios=document.getElementById("ecomentarios");var localizacion=$("#localizacion").val();var id_elocalizacion=document.getElementById("elocalizacion");var idioma=$("#idiomas_id").val();var id_eidioma=document.getElementById("eidiomas_id");var return_titulo=validate_text(titulo,id_etitulo,"El titulo es un valor obligatorio con un m&iacute;nimo de 10 caracteres",10);var return_comentarios=validate_text(comentarios,id_ecomentarios,"La descripci&oacute;n es campo obligatorio con un m&iacute;nimo de 10 caracteres", 10);var return_localizacion=validate_videotutorial(localizacion, id_elocalizacion, "La ubicaci&oacute;n del v&iacute;deo es incorrecta (&lt;iframe ...&gt;&lt;/iframe&gt;)");var return_idioma=validate_select(idioma,id_eidioma,"Selecciona el idioma del v&iacute;deo");if(number_languageSelected>0 && return_titulo && return_comentarios && return_localizacion && return_idioma){disableButtonSend("idSend");return true;}else{if(number_languageSelected==0){$("#elanguage").html("Tienes que seleccionar como m&iacute;nimo un lenguaje").show();}else{$("#elanguage").html("");}}
return false;}

function periodicity(value){if(value==1){document.getElementById("dayWeekly").style.display="none";document.getElementById("time").style.display="none";}else if(value==2){document.getElementById("dayWeekly").style.display="none";document.getElementById("time").style.display="inline";}else if(value==3){document.getElementById("dayWeekly").style.display="inline";document.getElementById("time").style.display="inline";}}

function enabledDisabled(file,id){if(file==undefined)
file="mail_ajax.php";$("#sendenable").attr("disabled","disabled");if(document.getElementById('enabledDisabledClock'))
$("#enabledDisabledClock").show();if($("#sendenable:checked").val()=="on"){var enable=1;}else{var enable=0;if(document.getElementById('blockED'))
$("#blockED").slideUp();}
$.post(file, {"type":$("#type").val(),"enable":enable, "id":id}, function(data){if(data.response==1)
{if($("#sendenable:checked").val()=="on"){$("#messageED").html("<span class='textEnabled'>ACTIVADO</span>");if(document.getElementById('blockED'))
$("#blockED").slideDown();}else{$("#messageED").html("<span class='textDisabled'>DESACTIVADO</span>");}
$("#sendenable").removeAttr("disabled");}if(document.getElementById('enabledDisabledClock'))
$("#enabledDisabledClock").hide();}, "json");}

function rowDelMail(id){$("#ico"+id).attr({src: "/img/ico_activity.gif", alt:"Eliminando", title:"Eliminando"});$.post("mail_ajax.php", {"type":$("#type").val(),"del":id}, function(data)
{if(data=="1"){$("#div"+id).hide();}else{$("#ico"+id).attr({src: "/img/ico_trash.png", alt:"Eliminar", title:"Eliminar"});}});}

function rowDelCurLevel(id){$("#ico"+id).attr({src: "/img/ico_activity.gif", alt:"Eliminando", title:"Eliminando"});$.post("curriculum_ajaxLevel.php", {"idc":$("#idCurriculum").val(),"idf":$("#idFreelance").val(),"del":id}, function(data)
{if(data=="1"){$("#div"+id).hide();}else{$("#ico"+id).attr({src: "/img/ico_trash.png", alt:"Eliminar", title:"Eliminar"});}});}

function rowUpdCurLevel(id){$("#icou"+id).attr({src: "/img/ico_activity.gif"});$.post("curriculum_ajaxLevel.php", {"idc":$("#idCurriculum").val(),"idf":$("#idFreelance").val(),"idu":id}, function(data)
{if(data.language>0){$("#language").val(data.language);$("input:radio[name=level][value="+data.level+"]").click();
$("#ta").val(data.ta);}}, "json");$("#icou"+id).attr({src: "/img/ico_update.png"});}

function rowDelCurIdiom(id){$("#ico"+id).attr({src: "/img/ico_activity.gif", alt:"Eliminando", title:"Eliminando"});$.post("curriculum_ajaxIdiom.php", {"idc":$("#idCurriculum").val(),"idf":$("#idFreelance").val(),"del":id}, function(data)
{if(data=="1"){$("#div"+id).hide();}else{$("#ico"+id).attr({src: "/img/ico_trash.png", alt:"Eliminar", title:"Eliminar"});}});}

function rowUpdCurIdiom(id){$("#icou"+id).attr({src: "/img/ico_activity.gif"});$.post("curriculum_ajaxIdiom.php", {"idc":$("#idCurriculum").val(),"idf":$("#idFreelance").val(),"idu":id}, function(data)
{if(data.idiom>0){$("#idiom").val(data.idiom);$("input:radio[name=talk][value="+data.talk+"]").click();
$("input:radio[name=written][value="+data.written+"]").click();$("#ta").val(data.ta);}}, "json");$("#icou"+id).attr({src: "/img/ico_update.png"});}

function mailSubmit(){$("#listAdded").html("<div class='clock'><img src='/img/ajaxActivity.gif' border='0'></div>");var language=$("#language").val();var sendmailtype=$("#sendmailtype").val();var sendmailday=$("#sendmailday").val();var sendmailhour=$("#sendmailhour").val();$("#listAdded").load("mail_ajax.php", {"type":$("#type").val(),
"language":language,
"sendmailtype":sendmailtype,
"sendmailday":sendmailday,
"sendmailhour":sendmailhour});}

var number_languageSelected=0;$(document).ready(function(){$("#selectLanguages .arrow").click(function(){addLanguageSelected(this)});$("#selectLanguages #languagesList").dblclick(function(){addLanguageSelected(this)});$("#selectLanguages .languages #languagesListSelected .languageSelected .languageDel").click(function(){removeLanguageSelected(this);});

function addLanguageSelected(mythis){$("#selectLanguages .languages #languagesList option:selected").each(function(){var newId=$(this).val();var exist=false;$("#selectLanguages .languages #languagesListSelected .languageSelected").each(function(){if($(this).attr("id")==newId){exist=true}});if(!exist){number_languageSelected+=1;$("#selectLanguages .languages #languagesListSelected").append("<div class='languageSelected' id='"+newId+"'><span class='languageDel'></span><span class=''>"+$(this).text()+"</span><input type='hidden' name='idl"+newId+"' value='1'></div>");$("#selectLanguages .languages #languagesList option[value="+$(this).val()+"]").attr('disabled','disabled');$("#selectLanguages .languages #languagesListSelected .languageSelected .languageDel").click(function(){removeLanguageSelected(this);});}});}

function removeLanguageSelected(mythis){var id=$(mythis).parent().attr("id");$("#selectLanguages .languages #languagesList option[value="+id+"]").removeAttr('disabled');number_languageSelected-=1;
$(mythis).parent().remove();}});function programadoresCheck(type,checked,id){if(checked==true)
checked=1;else
checked=0;$.post("/ajax/programadoresCheck.php", {"type":type, "checked":checked});if(id!=undefined){$("#"+id).slideUp();}}

function programmersCode_enableDisableInputs(type){if(type=="o3"){$("#eHomePageWhereIsFile div:nth-child(2)").addClass("form_titleObligatory");$("#eHomePageWhereIsFileUrl div:nth-child(2)").addClass("form_titleObligatory");}if(type=="o4"){$("#eHomePageWhereIsFile div:nth-child(2)").removeClass("form_titleObligatory");$("#eHomePageWhereIsFileUrl div:nth-child(2)").removeClass("form_titleObligatory");}}
function uc_showForm(idUser,idUnique,sectionIdContent){if($("#userContact_content"+idUnique).html()==""){$("#userContact_content"+idUnique).html("<div class='clock'><img src='/img/ajaxActivity.gif' border='0'></div>");$("#userContact_content"+idUnique).show();
var title="";if(document.getElementById("titleToContact_"+idUnique)){var title=$("#titleToContact_"+idUnique).html();}
$("#userContact_content"+idUnique).load("/ajax/userContact_showForm.php", {idUser:idUser, idUnique:idUnique, title:title, content:sectionIdContent},function(){if(document.getElementById("name_"+idUnique)){$("#name_"+idUnique).focus();}else{$("#title_"+idUnique).focus();}});}else{if($("#userContact_content"+idUnique).css("display")=="none"){$("#userContact_content"+idUnique).slideDown();if(document.getElementById("name_"+idUnique))
{$("#name_"+idUnique).focus();}else{$("#title_"+idUnique).focus();}}else{$("#userContact_content"+idUnique).slideUp();}}}

function validateForm(id){var name=1;var mail=1;if(document.getElementById('name_'+id)){name=validate_text($("#name_"+id).val(), document.getElementById("ename_"+id), 'El campo nombre es obligatorio', 1);mail=validate_email($("#mail_"+id).val(), document.getElementById("email_"+id), 1);}
var title=validate_text($("#title_"+id).val(), document.getElementById("etitle_"+id), 'El campo t&iacute;tulo es obligatorio', 2);var message=validate_text($("#ta_"+id).val(),document.getElementById("eta_"+id),"El campo de texto ha de contener como m&iacute;nimo 10 car&aacute;cteres",10);if(name==1 && mail==1 && title==1 && message==1)
return true;return false;}

function uc_sendForm(id,filePHP){if(filePHP==undefined)
filePHP="userContact_save.php"
filePHP=filePHP+"?"+new Date().getTime();if(validateForm(id)){$("#button_"+id).html();$.post("/ajax/"+filePHP, 
{id:$("#idtc_"+id).val(),
name:$("#name_"+id).val(),
surname:$("#surname_"+id).val(),
mail:$("#mail_"+id).val(),
title:$("#title_"+id).val(),
referer:$("#referer_"+id).html(),
message:$("#ta_"+id).val()},function(data){if(data.email){$("#email_"+id).html(data.email);$("#button_"+id).html("<input type='submit' value='Enviar Datos' onclick='uc_sendForm(\""+id+"\", filePHP)' class='button'>");$("#email_"+id).show();}else if(data.error){$("#userContactError"+id).html(data.error);$("#userContactError"+id).show();}else if(data.content){$("#userContact_content"+id).attr("class","block_ok")
$("#userContact_content"+id).html(data.content);}},"json"
);}
return false;}

function showFormComment(idanswer,section,idc,idv){if(document.getElementById("idshowForm_"+idanswer).style.display=='table' || document.getElementById("idshowForm_"+idanswer).style.display=='inline-block' || document.getElementById("idshowForm_"+idanswer).style.display=='inline'){document.getElementById("idshowForm_"+idanswer).style.display='none';}else{if(idlast!=0 && !document.forms["form_"+idlast]){document.getElementById("idshowForm_"+idlast).style.display='none';}
idlast=idanswer;document.getElementById("idshowForm_"+idanswer).style.display='inline-block';if(!document.forms["form_"+idanswer]){document.getElementById("idshowForm_"+idanswer).innerHTML="<div class='form center'><img src='/img/ajaxActivity.gif' border='0' /></div>";$.post("/ajax/ajax_showFormComment.php", {"section":section,"id":idc, "idanswer":idanswer, "v":idv}, function(data){$("#idshowForm_"+idanswer).html(data.content);stars();
comment_setFocus(idanswer,data.user);}, "json");}else{comment_setFocus(idanswer,user);}}}

function comment_setFocus(id,user){if(user==0)
$("form[name=formComment_"+id+"] input[name='nombre']").focus();else
$("form[name=formComment_"+id+"] textarea").focus();}
var idlast=0;var idlastUpd=0;var idlastSelect=0;var user=0;function showForm(id,path){if(document.forms["formUpd_"+idlastUpd]){$("#idshowFormUpd_"+id).hide();}if(document.getElementById("idshowForm_"+id).style.display=='table' || document.getElementById("idshowForm_"+id).style.display=='inline-block' || document.getElementById("idshowForm_"+id).style.display=='inline'){document.getElementById("idshowForm_"+id).style.display='none';}else{if(idlast!=0 && !document.forms["form_"+idlast]){document.getElementById("idshowForm_"+idlast).style.display='none';}
idlast=id;document.getElementById("idshowForm_"+id).style.display='inline-block';if(!document.forms["form_"+id]){document.getElementById("idshowForm_"+id).innerHTML="<div class='form center'><img src='/img/ajaxActivity.gif' border='0' /></div>";var title=document.getElementById("idT"+id).innerHTML;var title=title.replace(/&lt;/g,"<");var title=title.replace(/&gt;/g,">");$.post("/"+path+"/ajax_showForm.php", {"id":id, "title":title}, function(data){$("#idshowForm_"+id).html(data.content);user=data.user;
foros_setFocus(id,user);}, "json");}else{foros_setFocus(id,user);}
selectNew(id);}}

function showFormUpd(id,path){if(document.getElementById("idshowFormUpd_"+id).style.display=='table' || document.getElementById("idshowFormUpd_"+id).style.display=='inline'){document.getElementById("idshowFormUpd_"+id).style.display='none';}else{if(idlastUpd!=0 && !document.forms["formUpd_"+idlastUpd]){document.getElementById("idshowFormUpd_"+idlastUpd).style.display='none';}
idlastUpd=id;document.getElementById("idshowFormUpd_"+id).style.display='inline';if(!document.forms["formUpd_"+id]){document.getElementById("idshowFormUpd_"+id).innerHTML="<div class='form center'><img src='/img/ajaxActivity.gif' border='0' /></div>";$.post("/"+path+"/ajax_showFormUpd.php", {"id":id}, function(data){if(data.error)
$("#idshowFormUpd_"+id).html(data.error);else
$("#idshowFormUpd_"+id).html(data.content);user=data.user;
$("#ta"+id).focus();}, "json");}else{$("#ta"+id).focus();}}}

function foros_setFocus(id,user){if(user==0)
$("#name_"+id).focus();else if($("#titulo_"+id).val()=="")
$("#titulo_"+id).focus();else
$("#ta"+id).focus();}

function showFormAjax(idContenido){if(Conexion.responseText)
{document.getElementById(idContenido).style.display=js_display;document.getElementById(idContenido).innerHTML=Conexion.responseText;if(document.getElementById("form_nombre_"+idlast))
document.getElementById("form_nombre_"+idlast).focus();}else{document.getElementById(idContenido).style.display=js_display;document.getElementById(idContenido).innerHTML="";}}

function closeForms(){for(i=0;i<ids.length;i++)
{document.getElementById(ids[i]).style.display='none';}}

function selectNew(id){if(idlastSelect>0){$("#div"+idlastSelect+">div:first>div:first").removeClass("selected");}if(id){$("#div"+id+">div:first>div:first").addClass("selected");idlastSelect=id;}}

function timeleftUpd(){var value="";if(timeleft.length>0){for(var i=0;i<timeleft.length;i++)
{if(timeleft[i][1]!=0){if(timeleft[i][1]>0)
timeleft[i][1]=(timeleft[i][1]-1);else
timeleft[i][1]=0;value=secondsToHours(timeleft[i][1])
$("#time"+timeleft[i][0]).html(value);}else if(timeleft[i][2]!=-1){pathArray=window.location.pathname.split('/');if(timeleft[i][2]==1)
{$("#btnUpd_"+timeleft[i][0]).attr({"onclick":"javascript:showForm("+timeleft[i][0]+", '"+pathArray[1]+"')"}).html("Responder");}else if(timeleft[i][2]==2){$("#btnUpd_"+timeleft[i][0]).attr({"onclick":"javascript:showForm("+timeleft[i][0]+", '"+pathArray[1]+"')"}).html("Comentar");}
timeleft[i][2]=-1;$("#time"+timeleft[i][0]).parent().hide();}}
setTimeout(timeleftUpd,998);}}
$(document).ready(function(){$(".forosVotar .img").click(function(event){var id=$(this).parent().parent().parent().parent().parent().parent().attr("id");if($(this).hasClass("votaUp")){var type="u";}else if($(this).hasClass("votaDown")){var type="d";}
var value=$("#v"+id.substring(3)).html();$("#v"+id.substring(3)).html("<div class='clock' style='padding:0px;'><img src='/img/ico_activity.gif' border='0' width='16' height='16'></div>");$.post("/foros/ajax_votar.php", {"id":id.substring(3), "type":type, "value":value}, function(data){$("#v"+id.substring(3)).html(data.newValue);if(data.err){$("#forosVote").hide();$("#forosVote").html("<h4>"+data.err+"</h4><br /><p style='text-align:center;'>Haz clic en el recuadro para cerrarlo</p>");$("#forosVote").addClass("block_info");
$("#forosVote").css({"top":(event.pageY+10), "left":event.pageX, "width":"300px"}).fadeIn();$("#forosVote").click(function(){$("#forosVote").fadeOut()});}}, "json");});
$("#rf").click(function(){$("#rf_content").html('').addClass("clockWithImg16").css("margin-left","10px");$.post("/foros/ajax_removeFilter.php", function(){location.reload();});});});
$(document).ready(function(){var messageSelected=0;$("#messagesList .group").click(function(event){var idGroup=$(this).attr("id");var id=idGroup.substring(1);var target = $(event.target);if(target.is(":checkbox")){if(target.is(":checked"))
{$("#"+idGroup).addClass("groupSelected");messageSelected++;}else{$("#"+idGroup).removeClass("groupSelected");messageSelected--;}
showButtons();}else{var idMessage="m"+id;var type=$("#type").val();if($("#"+idMessage).css("display")=="none"){if($("#"+idMessage).html()=="")
{$("#"+idMessage).html("<div class='clock'><img src='/img/ajaxActivity.gif' border='0'></div>");$("#"+idMessage).slideDown();
$.post("/ajax/userContact_getMessage.php", {"idMessage":id, "type":type}, function(data){if(data.content){$("#"+idMessage).html(data.content);$("#"+idGroup).css({"font-weight":"normal"});
editor_viewImages();}else if(data.error){$("#"+idMessage).html("<div class='block_ko'>"+data.error+"</div>");}},"json");}else{$("#"+idMessage).slideDown();}}else{$("#"+idMessage).slideUp();}}});$("#messagesList .buttons .buttonAll").click(function(event){messageSelected=0;$("#messagesList .group").each(function(index){var idGroup=$(this).attr("id");var id=idGroup.substring(1);$("#"+idGroup).addClass("groupSelected");
$("input[name=ck"+id+"]").attr('checked',true);messageSelected++;});showButtons();});$("#messagesList .buttons .buttonNone").click(function(event){$("#messagesList .group").each(function(index){var idGroup=$(this).attr("id");var id=idGroup.substring(1);if($("input[name=ck"+id+"]").is(":checked")){$("input[name=ck"+id+"]").attr('checked',false);$("#"+idGroup).removeClass("groupSelected");}});messageSelected=0;
showButtons();});

$("#messagesList .buttons .buttonUnreaded").click(function(event){var type=$("#type").val();$("#messagesList .group").each(function(index){var idGroup=$(this).attr("id");var id=idGroup.substring(1);if($("input[name=ck"+id+"]").is(":checked")){if($("#"+idGroup).css("font-weight")=="normal" || $("#"+idGroup).css("font-weight")==400)
{$.post("/ajax/userContact_readed.php", {"idMessage":id, "type":type, "unread":"1"}, function(data){if(data.content=="1"){$("#"+idGroup).css({"font-weight":"bold"});messageUnselect(idGroup,id);}},"json");}else{messageUnselect(idGroup,id);}}});});

$("#messagesList .buttons .buttonReaded").click(function(event){var type=$("#type").val();$("#messagesList .group").each(function(index){var idGroup=$(this).attr("id");var id=idGroup.substring(1);if($("input[name=ck"+id+"]").is(":checked")){if($("#"+idGroup).css("font-weight")=="bold" || $("#"+idGroup).css("font-weight")==700)
{$.post("/ajax/userContact_readed.php", {"idMessage":id, "type":type, "read":"1"}, function(data){if(data.content=="1"){$("#"+idGroup).css({"font-weight":"normal"});messageUnselect(idGroup,id);}},"json");}else{messageUnselect(idGroup,id);}}});});

$("#messagesList .buttons .buttonDelete").click(function(event){var type=$("#type").val();if(type=="t"){var confirmacion=confirm("Estas seguro de eliminar las notas seleccionadas?")}else{var confirmacion=confirm("Estas seguro de eliminar los mensajes seleccionados?");}if(confirmacion){$("#messagesList .group").each(function(index){var idGroup=$(this).attr("id");var id=idGroup.substring(1);if($("input[name=ck"+id+"]").is(":checked")){$.post("/ajax/userContact_delete.php", {"idMessage":id, "type":type}, function(data){if(data.content=="1"){$("#"+idGroup).css({"text-decoration":"line-through"});messageUnselect(idGroup,id);}},"json");}});}});function messageUnselect(idGroup,id){$("input[name=ck"+id+"]").removeAttr('checked');$("#"+idGroup).removeClass("groupSelected");
messageSelected--;showButtons();}

function showButtons(){if(messageSelected>0){$("#messagesList .buttons .buttonAll").hide();$("#messagesList .buttons .buttonNone").show();$("#messagesList .buttons .buttonReaded").show();$("#messagesList .buttons .buttonUnreaded").show();$("#messagesList .buttons .buttonDelete").show();}else{$("#messagesList .buttons .buttonAll").show();$("#messagesList .buttons .buttonNone").hide();$("#messagesList .buttons .buttonReaded").hide();$("#messagesList .buttons .buttonUnreaded").hide();$("#messagesList .buttons .buttonDelete").hide();}}

$(".programmer .programmerContact").click(function(){var idProgrammer=$(this).parent().parent().parent().attr("id");uc_showForm(idProgrammer,idProgrammer);});$(".tablonList .programmerContact").click(function(){var idUser=$(this).parent().attr("id");var id=$(this).attr("id");uc_showForm(idUser,id);});$(".listRowJob .programmerContact>span").click(function(){var idUser=$(this).parent().parent().parent().attr("id");var id=$(this).attr("id");uc_showForm(idUser,id);});$(".usuario .programmerContact").click(function(){var idUser=$(this).parent().parent().parent().attr("id");uc_showForm(idUser,idUser);});});
$(document).ready(function(){$(".datepicker").focus(function(){if($("#datepicker").length && $('#datepicker').is(":hover")){}else{if(checkDate_spanish($(this).val())==true){var values=$(this).val().split("/");showCalendar(values[2],values[1]-1,values[0]);}else{showCalendar();}
$("#datepicker").offset({top:$(this).offset().top+25, left:$(this).offset().left});object=$(this);}});$(".datepicker").blur(function(){if($('#datepicker').is(":hover")){}else{$("#datepicker").fadeOut();}});$(".datepicker").on("keyup change",function(){if(checkDate_spanish($(this).val())==true){var values=$(this).val().split("/");showCalendar(values[2],values[1]-1,values[0]);}});function showCalendar(year,month,day){if($("#datepicker").length==0){$("body").append("<div id='datepicker'><table><caption></caption><thead><tr><th>Lu</th><th>Ma</th><th>Mi</th><th>Ju</th><th>Vi</th><th>Sa</th><th>Do</th></tr></thead><tbody></tbody></table></div>");}
$("#datepicker").fadeIn();var now=new Date();var dayNow=now.getDate();var select=0;if(year==undefined || month==undefined){var d=new Date();}else{if(month==12){month=0;year++;}if(month==-1){month=11;year--;}
var d=new Date(year,month);if(day!=undefined)
select=day;}
var monthShow=d.getMonth();var yearShow=d.getFullYear();var firstDayDate=new Date(d.getFullYear(), d.getMonth(),1);var firstDay=firstDayDate.getDate();var dayWeek=firstDayDate.getDay()+7;var lastDayDate=new Date(d.getFullYear(), d.getMonth() + 1,0);var lastDay=lastDayDate.getDate();$("#datepicker table caption").html("<span>&lt;&lt;</span><span>"+months[monthShow]+" "+yearShow+"</span><span>&gt;&gt;</span>");$("#datepicker table tbody tr").remove();$("#datepicker table tbody").append("<tr></tr>");var last_cell=dayWeek+lastDay
var day=0;for(var i=1;i<=42;i++){if(i==dayWeek)
{day=1;}if(i<dayWeek || i>=last_cell){$("#datepicker table tbody tr:last-child").append("<td></td>");}else{if(day==select)
$("#datepicker table tbody tr:last-child").append("<td class='select d'>"+day+"</td>");else if(day==dayNow && monthShow==now.getMonth())
$("#datepicker table tbody tr:last-child").append("<td class='today d'>"+day+"</td>");else
$("#datepicker table tbody tr:last-child").append("<td class='d'>"+day+"</td>");day++;}if(i%7==0){if(i>last_cell)
{break;}
$("#datepicker table tbody").append("<tr></tr>");}}
$("#datepicker table .d").click(function(){object.val($(this).html()+"/"+(monthShow+1)+"/"+yearShow);$("#datepicker").fadeOut();});$("#datepicker table caption span:first-child").click(function(){object.focus();showCalendar(yearShow,monthShow-1)});$("#datepicker table caption span:last-child").click(function(){object.focus();showCalendar(yearShow,monthShow+1)});}});
var socket;var keys={shift:false,ctrl:false};var textInTextarea=false;function startSocket(){if(!$("#usuario").val()){alert("Introduce un usuario");}else{if(!("WebSocket" in window)){alert("Tu navegador no soporta web sockets");}else{var host = "ws://www.lawebdelprogramador.com:8081";socket=new WebSocket(host);if(socket){connected();$("#data").focus();

socket.onopen=function(){var msg = {type:1,
user:$("#usuario").val(),
token:getCookie("token"),
id:$("input[name=idp]").val(),
idl:$("input[name=idl]").val()};socket.send(JSON.stringify(msg));
showButtonLoadLastMessages();}

socket.onmessage=function(msg){var msgJson=JSON.parse(msg.data);if(msgJson.type==1){showServerUsers(msgJson.data);if($("#audio_newUser:checked").length)
{audio_user.currentTime=0;audio_user.play();}}else if(msgJson.type==2){var moveScroll=false;if($("#messages").innerHeight()==$("#messages")[0].scrollHeight){moveScroll=true;}else{if($("#messages").scrollTop()+$("#messages").innerHeight()==$("#messages")[0].scrollHeight){moveScroll=true;}}
showServerResponse(msgJson.data);if($("#audio_message:checked").length && msgJson.data.a!=-1){audio_message.currentTime=0;audio_message.play();}if(moveScroll==true){$("#messages").scrollTop($("#messages")[0].scrollHeight);$("#messages").removeClass("anima");}else{$("#messages").removeClass("anima");setTimeout(function(){$("#messages").addClass("anima");},1);}}else if(msgJson.type==4){if(msgJson.write==1)
{$("#idc"+msgJson.idc+" img").after('<img src="/img/ico_edit.gif" width="16" height="16" class="icoEdit">');}else{$("#idc"+msgJson.idc).find(".icoEdit").remove();}}}

socket.onclose=function(){showServerResponse({"idm":0,"user":"System", "date":"", "msg":"La conexión con el servidor se ha cerrado", "pi":"/img/logoCircle.png"});$("#messages").scrollTop($("#messages")[0].scrollHeight);
disconnected();$("#messages p.button").remove();}}else{console.log("invalid socket");}

$("#sendtext").on('click',function(){if(($("#data").val()).trim() == "" || ($("#usuario").val()).trim()==""){return;}
$("#usuario").prop('disabled', true);var msg = {type:2,
data:($("#data").val()).trim()};$("#messages").scrollTop($("#messages")[0].scrollHeight);
socket.send(JSON.stringify(msg));$("#data").val("").focus();
$("#data").keyup();});
$("#sendcode").on('click',function(){if(($("#data").val()).trim() == "" || ($("#usuario").val()).trim()==""){return;}
$("#data").val("[code]"+($("#data").val()).trim()+"[/code]");$("#sendtext").click();});$("#data").on("keydown",function(event){if(event.keyCode==16)
keys["shift"]=true;if(keys["shift"]==false && event.keyCode==13){$("#sendtext").click();return false;}});$("#data").on("keyup",function(event){if(event.keyCode==16)
keys["shift"]=false;if(textInTextarea==false && $("#data").val()!=""){textInTextarea=true;var msg = {type:4,
write:1};socket.send(JSON.stringify(msg));}else if(textInTextarea==true && $("#data").val()==""){textInTextarea=false;var msg = {type:4,
write:0};socket.send(JSON.stringify(msg));}});function showServerResponse(msg){if(msg.idm==0 || $("#"+msg.idm).length==0){if($("#messages p").length==0)
{showButtonLoadLastMessages();}
var p=document.createElement('p');p.innerHTML=messageFormat(msg);if(msg.idm!=0)
p.setAttribute("id", msg.idm);document.getElementById('messages').appendChild(p);
$("#messages .right.img.cancel").unbind("click").click(function(){chat_showMessagesOffensive($(this).parent("p").attr("id"),"Si crees que este mensaje es <b>ofensivo</b>, o <b>no cumple con el objetivo del chat</b>, o simplemente no tiene ningún sentido, coméntanoslo para eliminar el mensaje y contactar con el usuario de dicho mensaje.<p>Estas seguro que quieres eliminar este mensaje?</p>",200,100);});}}

function showServerUsers(users){var result="<ul>";for(i=0;i<users.length;i++){result+="<li id='idc"+users[i][1][4]+"'>";if(users[i][1][3])
result+="<img src='"+users[i][1][3]+"'>";else
result+="<img src='/img/anonymouse.png'>";if(users[i][1][2]==0){result+="<a href='/programadores/"+users[i][1][1]+"' target='_blank'>"+users[i][1][0]+"</a></li>";}else{result+="<img src='/img/ico_prohibit_ko.png' class='removeUser' onclick=\"removeUser('"+users[i][1][2]+"')\">"+users[i][1][0]+"</li>";}}
result+="</ul>";$("#users").html(result);}}}}

function messageFormat(msg){var content="";if(msg.pi)
content+="<div class='left'><img src='"+msg.pi+"'></div>";else
content+="<div class='left'><img src='/img/anonymouse.png'></div>";content+="<div class='left'>";if(msg.userid==0 || msg.userid==undefined)
content+="<span class='f_redDark'>"+msg.user+"</span>";else
content+="<span><a href='/programadores/"+msg.userid+"' target='_blank'>"+msg.user+"</a></span>";content+="</div>";
content+="<div class='right'>"+msg.date+"</div>";if(msg.idm!=0){content+="<div class='right img cancel' title='Este mensaje es ofensivo\no no cumple con el objetivo del chat'></div>";}else{content+="<div class='right img'></div>";}
content+="<div>"+msg.msg+"</div>";return content;}
function closeSocket(){socket.close();}

function removeUser(user){msg={"type":3,
"user":user}
socket.send(JSON.stringify(msg));}

function connected(){$("#texto,#sendtext,#sendcode,#desconectar,#data").removeAttr("disabled");$("#usuario,#conectar").attr("disabled","disabled");}
function disconnected(){$("#texto,#sendtext,#sendcode,#desconectar,#data").attr("disabled","disabled");$("#usuario,#conectar").removeAttr("disabled");
$("#users").html("");}
$(document).ready(function(){$(".chat_header>div:nth-child(2).img img").click(function(){if($(".chat-wrapper").hasClass("maximize")){$(".chat-wrapper").removeClass("maximize");}else{$(".chat-wrapper").addClass("maximize");}});$(".chat_header>div>div.img:last img").click(function(){$(".chat_header .menuConfig").toggle();});

$("#audio_message").click(function(){if($("#audio_message:checked").length){setCookie("chat_m","1",365);}else{setCookie("chat_m","0",365);}});$("#audio_newUser").click(function(){if($("#audio_newUser:checked").length){setCookie("chat_nu","1",365);}else{setCookie("chat_nu","0",365);}});});
function chat_showMessagesOffensive(idm,text,width,height){if(parseInt(idm)>0){showMessage_OkCancel("Eliminar mensaje","Eliminar mensaje",text,width,height);$("#messageOkButton").unbind("click").click(function(){$.post("/ajax/chat_messageOffensive.php", {"idm":idm});$("#"+idm).hide();
layerClose();});}}
function chat_cleaner(){$("#messages").html("");return false;}
function showButtonLoadLastMessages(){$("#messages").prepend("<p class='button'>Descargar mensajes anteriores&nbsp;&nbsp;<span></span></p>");$("#messages p.button").click(function(){loadMessages(this);})}
function loadMessages(e){if($(e).hasClass("disabled")){return false;}else{var id=0;$("#messages p").each(function(){if($(this).attr("id")){id=$(this).attr("id");return false;}});if(id!=0){$("p.button span").addClass("clockWithImg16").css({"vertical-align":"top"});$(e).addClass("disabled");
$.post("/chat/loadMessages.php",{idm:id,idl:$("input[name=idl]").val()},function(data){if(data && data.messages){for(var i=0;i<data.messages.length;i++)
{var p=document.createElement('p');p.innerHTML=messageFormat(data.messages[i]);if(data.messages[i].idm!=0)
p.setAttribute("id", data.messages[i].idm);document.getElementById('messages').appendChild(p);
$(p).insertAfter(e);}
$(e).removeClass("disabled");$("p.button span").removeClass("clockWithImg16");}},"json");}}}
var valueAutocompletar="";function autocompletar(){if(getCookie("pdfDirTags")){var tagsSeleccionados=decodeURIComponent(escape(getCookie("pdfDirTags")));tagsSeleccionados=tagsSeleccionados.split(",");
showTags();}else{var tagsSeleccionados=new Array();}
var sorted=listTags.sort();$(".autocompletar input[type=text]").keyup(function(e){if(e.which==13){tagAdd($(this).val());}else{buscar($(this));}});$(".autocompletar input[type=button]").click(function(){tagAdd($(".autocompletar input[type=text]").val());});
$(".autocompletar input[type=text]").dblclick(function(){if($(".autocompletar input[type=text]").val()==""){showAllTags($(this));}});function tagAdd(tag){if(sorted.indexOf(tag)!=-1 && tagsSeleccionados.indexOf(tag)==-1){tagsSeleccionados.push(tag);setCookie("pdfDirTags",tagsSeleccionados,60);
location.reload();}}

function buscar(objeto){objeto.css("color","Black");valueAutocompletar=objeto.val();if(valueAutocompletar){var positionStart=sorted.findIndex(findMyWord);if(positionStart>=0){var li="";var re=new RegExp("^"+valueAutocompletar+"+", "i");for(var i=positionStart;i<sorted.length;i++){if(re.test(sorted[i]))
li+="<li>"+sorted[i]+"</li>";else
break;}
showLi(objeto,li);}else{objeto.parent().find("ul").hide();objeto.css("color","Red");}}else{objeto.parent().find("ul").hide();}}

function showAllTags(objeto){var li="";for(var i=0;i<sorted.length;i++){li+="<li>"+sorted[i]+"</li>";}
showLi(objeto,li);}

function showLi(objeto,li){objeto.parent().find("ul").html(li).show();$(".autocompletar ul li").unbind("click").click(function(){tagAdd($(this).html());});}
$(".autocompletar input[type=text]").focus(function(){if($(this).val()!=""){buscar($(this));$(this).select();}});$(document).click(function(){if($(".autocompletar input[type=text]").is(":focus")==false){$(".autocompletar").find("ul").hide();}});function findMyWord(element){var re=new RegExp("^"+valueAutocompletar+"+","i");if(re.test(element))
return true;return false;}

function showTags(){$(".autocompletar .tags").html("");var tagsSeleccionadosSorted=tagsSeleccionados.sort();for(var i=0;i<tagsSeleccionadosSorted.length;i++){$(".autocompletar .tags").append("<div>"+tagsSeleccionadosSorted[i]+"<span id='"+tagsSeleccionadosSorted[i]+"'>X</span></div>");}
$(".autocompletar .tags span").unbind("click").click(function(){tagsSeleccionados.splice( tagsSeleccionados.indexOf($(this).attr("id")), 1 );setCookie("pdfDirTags",tagsSeleccionados,60);
location.reload();});}}
function stars(){$(".starsSel ul li").unbind("click");$(".starsSel ul li").click(function(){$(this).addClass("selected");var starsSel=$(this).parent().parent();$(this).prevAll("li").addClass("selected");
$(this).nextAll("li").removeClass("selected");var assessment=$(this).index()+1;starsSel.find("input[name=stars]").val(assessment);if(assessment==1)
starsSel.find("span").html("<span class='f_red'>Malo</span>");else if(assessment==2)
starsSel.find("span").html("Regular");else if(assessment==3)
starsSel.find("span").html("Bien");else if(assessment==4)
starsSel.find("span").html("Bueno");else if(assessment==5)
starsSel.find("span").html("<span class='f_green'>Excelente</span>");});}
$(document).ready(function(){stars();$(".compressed").each(function(){if($(this).height()>50){$(this).append("<div class='mas'>+</div>").addClass("min");}
$(this).show();});
$(".compressed .mas").click(function(){if($(this).parent("div").hasClass("min")){$(this).parent("div").removeClass("min");$(this).html("-");}else{$(this).parent("div").addClass("min");$(this).html("+");}});});

function validate_maxLenght(text,id_eobj,error,charLenght){if(text.length>charLenght){id_eobj.innerHTML=error;id_eobj.style.display="block";
return 0;}else{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}}

function validate_text(text,id_eobj,error,charLenght){if(charLenght==undefined)
charLenght=0;if(text=="" || (charLenght>0 && text.length<charLenght)){id_eobj.innerHTML=error;id_eobj.style.display="block";
return 0;}else{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}}

function validate_email(mail,id_eobj,obligatory){if(mail=="" && obligatory==0){if(id_eobj)
{id_eobj.innerHTML="";id_eobj.style.display="none";}
return 1;}if(isValidMail(mail,obligatory)==true){if(id_eobj)
{id_eobj.innerHTML="";id_eobj.style.display="none";}
return 1;}if(id_eobj){id_eobj.innerHTML="Indica una direcci&oacute;n de correo v&aacute;lida";id_eobj.style.display="block";}
return 0;}

function validate_url(url,id_eobj,obligatory){if(url=="" && obligatory==0){if(id_eobj)
{id_eobj.innerHTML="";id_eobj.style.display="none";}
return 1;}if(isValidUrl(url,obligatory)==true){if(id_eobj)
{id_eobj.innerHTML="";id_eobj.style.display="none";}
return 1;}if(id_eobj){id_eobj.innerHTML="Indica una direcci&oacute;n web v&aacute;lida";id_eobj.style.display="block";}
return 0;}

function validate_radio(nameForm,name,id_eobj,error){var i;for(i=0;i<eval("document."+nameForm+"."+name+".length");i++){if(eval("document."+nameForm+"."+name+"[i].checked"))
{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}} 
id_eobj.innerHTML=error;id_eobj.style.display="block";
return 0;}

function isValidDate(day,month,year){var dteDate;month=month-1;
dteDate=new Date(year,month,day);return ((day==dteDate.getDate()) && (month==dteDate.getMonth()) && (year==dteDate.getFullYear()));}

function validate_fecha(value,id_eobj,showError,ControlDaySupActual){if(ControlDaySupActual==undefined){ControlDaySupActual=true;}
var patron=new RegExp("^([0-9]{1,2})([/])([0-9]{1,2})([/])(19|20)+([0-9]{2})$");if(value.search(patron)==0){values=value.split("/");if(isValidDate(values[0],values[1],values[2]))
{var d=new Date();var fechaActual=new Date(d.getFullYear(), d.getMonth(), d.getDate(),0,0,0);var fechaUsuario=new Date(values[2],(values[1]-1),values[0],0,0,0);if(ControlDaySupActual==true && fechaUsuario>fechaActual){if(showError)
{id_eobj.innerHTML="La fecha es posterior a la actual";}}else if(ControlDaySupActual==false && fechaUsuario<fechaActual){if(showError)
{id_eobj.innerHTML="La fecha es anterior a la actual";}}else{if(showError){id_eobj.innerHTML="";id_eobj.style.display="none";}
return 1;}}elseif(showError)
id_eobj.innerHTML="La fecha es incorrecta.";}elseif(showError)
id_eobj.innerHTML="El formato de fecha es incorrecto (dd/mm/yyyy)";if(showError)
id_eobj.style.display="block";return 0;}

function checkDate_spanish(fecha){var patron=new RegExp("^([0-9]{1,2})([/])([0-9]{1,2})([/])(19|20)+([0-9]{2})$");if(fecha.search(patron)==0){var values=fecha.split("/");if(isValidDate(values[0],values[1],values[2])){return true;}}
return false;}

function validate_dateInOneYear(value,id_eobj){var patron=new RegExp("^([0-9]{1,2})([/])([0-9]{1,2})([/])(19|20)+([0-9]{2})$");if(value.search(patron)==0){values=value.split("/");if(isValidDate(values[0],values[1],values[2]))
{var d=new Date();var fechaActual=new Date(d.getFullYear(), d.getMonth(), d.getDate(),0,0,0);var fechaMasUnAno=new Date(d.getFullYear(), d.getMonth()+12, d.getDate(),0,0,0);var fechaUsuario=new Date(values[2],(values[1]-1),values[0],0,0,0);if(fechaUsuario>fechaMasUnAno)
id_eobj.innerHTML="La fecha no puede ser superior a un a&ntilde;o";else if(fechaUsuario<fechaActual)
id_eobj.innerHTML="la fecha no puede ser inferior a hoy";else if(fechaUsuario==fechaActual)
id_eobj.innerHTML="La fecha de finalizaci&oacute;n no puede ser hoy";else{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}}else
id_eobj.innerHTML="La fecha es incorrecta";}else
id_eobj.innerHTML="El formato de fecha es incorrecto (dd/mm/yyyy)";id_eobj.style.display="block";
return 0;}

function isValidUrl(url,obligatory,ftp){if(obligatory==undefined)
obligatory=0;if(ftp==undefined)
ftp=0;if(url=="" && obligatory==0)
return true;if(ftp)
var pattern = /^(http|https|ftp)\:\/\/[a-z0-9\.-]+\.[a-z]{2,4}/gi;else
var pattern = /^(http|https)\:\/\/[a-z0-9\.-]+\.[a-z]{2,4}/gi;if(url.match(pattern))
return true;else
return false;}

function isValidMail(mail,obligatory){if(obligatory==undefined)
obligatory=0;if(mail=="" && obligatory==0)
return true;var patron=new RegExp(/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9_\-])+\.)+([a-zA-Z0-9]{2,15})$/);if(patron.test(mail))
return true;else
return false;}

function validate_select(text,id_eobj,error){if(text=="0")
{id_eobj.innerHTML=error;id_eobj.style.display="block";
return 0;}else{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}}

function trim(value){return value.replace(/^\s+/g,'').replace(/\s+$/g,'')}

function disableButtonSend(id){if(id=="" || id==undefined){id="idSend";}
button=document.getElementById(id);button.disabled=true;}

function setfocusForm(formularioNombre,campo){if(!formularioNombre)
formularioNombre=0;if(campo)
document.forms[formularioNombre].elements[campo].focus();else{if(document.forms[formularioNombre]){for(i=0;i < document.forms[formularioNombre].length;i++)
{if(document.forms[formularioNombre][i].type!="hidden" && document.forms[formularioNombre][i].name!=undefined){document.forms[formularioNombre].elements[i].focus();break;}}}}}
function validate_videotutorial(text,id_eobj,error){if(validate_iframe(text)==""){id_eobj.innerHTML=error;id_eobj.style.display="block";
return 0;}else{id_eobj.innerHTML="";id_eobj.style.display="none";
return 1;}}

function validate_iframe(str){if(str.search(/<iframe/i)>=0 && str.search(/<\/iframe>/i)>=0){var startVideo=str.search(/<iframe/i);var endVideo=str.search(/<\/iframe>/i)-startVideo+9;return str.substr(startVideo,endVideo);}
return "";}

function setCursorAtEnd(id){var obj = $("#"+id),
val=obj.val();obj.focus().val("").val(val);
obj.scrollTop(obj[0].scrollHeight);}

function prepareStringToRegExp(str){str=str.replace(/\(/g,"\\(");str=str.replace(/\)/g,"\\)");
return str;}

function parse_url(url){var pattern=RegExp("^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\?([^#]*))?(#(.*))?");var matches=url.match(pattern);var scheme="";var basename="";var query="";if(matches[2])
scheme=matches[2];if(matches[5]){var start=url.lastIndexOf("/")+1;var end=url.indexOf("?");if(end>0)
basename=url.substr(start,end-start);else
basename=url.substr(start);}if(matches[7])
query=matches[7];return {scheme: scheme,
authority: matches[4],
path: matches[5],
basename: basename,
query: query,
fragment: matches[9],};}

function youtubeGetKey(url){var video="";var parseUrl=parse_url(url);if(url.indexOf("/embed/")!=-1 || url.indexOf("/youtu.be/")!=-1){video=parseUrl["basename"];}else if(url.indexOf("/watch?")){querys=parseUrl["query"].split("&");for(var query in querys)
{values=querys[query].split("=");if(values[0].length && values[0]=="v" && values[1].length){video=trim(values[1]);}}}if(video.length!=11)
return ""
return video}
function showImage(image,width,height){var bodyWidth=width;if(width>$(window).width()){bodyWidth=$(window).width()-60;height=height*bodyWidth/width;}
var heightScreen=($(window).height())-60;layerShowClock();
$("#layerc").width(bodyWidth);$("#layerc").html("\
<div class='layer-wrapper center'>\
<img src='' style='max-width:"+bodyWidth+"px;max-height:"+heightScreen+"px'>\
</div>\
<div class='button-close'>x</div>");$("#layerc img").attr("src", image).load(function(){$("#layerc").show();layerShow();});$(".button-close").click(function(){layerClose();});}
$(document).ready(function(){$(".blockOptions div").click(function(){idForm=$(this).parents('form:first').attr("id");$("#"+idForm+" .errorForm").remove();id=$(this).attr("id");
$(".blockOptions div").each(function(){$(this).removeClass("selected")});$("#"+id).addClass("selected");
$(".o1").hide();$(".o2").hide();
$(".o3").hide();$(".o4").hide();
$("."+id).show();programmersCode_enableDisableInputs(id);
$("#option").val(id);});

$("form[name='formProgrammersAdd'] input[value='visitar']").click(function(){if(!$(this).hasClass("disabled")){var domain=$(this).parent("div").prev().html();var url=$(this).prev().val();window.open(domain+url);}});$(".programadoresSocialNetwork input[type='text']").keyup(function(){if($(this).val().length>0){$(this).next("input[type='button']").removeClass("disabled");}else{$(this).next("input[type='button']").addClass("disabled");}});});

function showMessage_OkCancel(title,acceptButton,text,width,height){var bodyWidth=width;if(width>$(window).width()){bodyWidth=$(window).width()-60;height=height*bodyWidth/width;}
layerShowClock();$("#layerc").width(bodyWidth);
$("#layerc").html("\
<div class='title'>\
"+title+"\
</div>\
<div class='text'>\
"+text+"\
</div>\
<div class='buttons'><input type='button' class='button' value='"+acceptButton+"' id='messageOkButton'>&nbsp;<input type='button' class='button' value='Cancel'></div>\
");layerShow();
$("#layerc input[type=button][value=Cancel]").click(function(){layerClose();});}
$(document).ready(function(){if($("#utilDig input[name=d]").val()){var values={domain:$("#utilDig input[name=d]").val()};sendForm("dig_ajax.php",values);}if($("#utilDigP input[name=d]").val()){$("#utilResult div").each(function(){var id=$(this).attr("id");$("#"+id+" span").addClass("clockWithImg16");$.post("dig-propagacion_ajax.php", {id:id, domain:$("#utilDigP input[name=d]").val(), type:$("#utilDigP select[name=type]").val()}, function(data){if(data.id){$("#"+data.id+" span").removeClass("clockWithImg16");if(data.result){$("#"+data.id+" span").addClass("oks").html(data.result);}else{$("#"+data.id+" span").addClass("kos");}}},"json");});}if($("#utilDNS input[name=d]").val()){var values={domain:$("#utilDNS input[name=d]").val()};sendForm("dns-inversa_ajax.php",values);}if($("#utilIp input[name=ip]").val()){var values={ip:$("#utilIp input[name=ip]").val()};sendForm("ip_ajax.php",values);}if($("#utilWhois input[name=d]").val()){var values={domain:$("#utilWhois input[name=d]").val()};sendForm("whois_ajax.php",values);}
$("#md5 input[type=button]").click(function(){if($("#md5 textarea").val()){var values={text:$("#md5 textarea").val()};sendForm("md5_ajax.php",values);}});$("#sha1 input[type=button]").click(function(){if($("#sha1 textarea").val()){var values={text:$("#sha1 textarea").val()};sendForm("sha1_ajax.php",values);}});$("#md5 #file").change(function(){sendFile("/utilidades/md5-archivo_ajax.php");});
$("#sha1 #file").change(function(){sendFile("/utilidades/sha1-archivo_ajax.php");});
$("#codi").click(function(){var values={text:$("#base64 textarea").val(), type:"co"};sendForm("base64_ajax.php",values);});$("#encodi").click(function(){var values={text:$("#base64 textarea").val(), type:"de"};sendForm("base64_ajax.php",values);});});
function sendForm(file,values){$("#utilResult").addClass("clockWithImg32");$.post(file,values,function(data){$("#utilResult").removeClass("clockWithImg32");if(data.result){$("#utilResult").html(data.result);}else if(data.error){$("#utilResult").html(data.error);}else{$("#utilResult").html("");}},"json");}
function sendFile(file){$("#utilResult").addClass("clockWithImg32");var formData=new FormData();formData.append("file",$("#file")[0].files[0]);
$.ajax({url:file,
type:"POST",
data:formData,
dataType:"json",
contentType:false,
processData:false,
cache:false}).done(function(data){$("#utilResult").removeClass("clockWithImg32");if(data.result)
$("#utilResult").html(data.result);else
$("#utilResult").html("No se ha recibido ninguna archivo");});}
