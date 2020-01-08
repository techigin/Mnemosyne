$(document).ready(function(){
    $('select').formSelect();
    $('.datepicker').datepicker({
            selectMonths: true,
            selectYears: 200,
            format: 'mm/dd/yyyy'
        });
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('.scrollspy').scrollSpy();
  });
