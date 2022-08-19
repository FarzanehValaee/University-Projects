$(document).ready(function() {

        
    $(".submit").attr('disabled','disabled');
    
    $.protip();


    $(".checked").iCheck({
        checkboxClass:'icheckbox_flat-blue'
    });
    

    $('input:checkbox').on('ifToggled', function() {
        if($(this).is(':checked'))
        {
            $(".submit").removeAttr('disabled');
        }
        else
        {
            $(".submit").attr('disabled','disabled');
        }

    });


    var clock = $('.myclock').FlipClock(5*60,{

        countdown:true ,
        callbacks: {
            stop: function () {
                console.log("end");

                swal({
                    title:"time out!!!!" ,
                    text: "refresh the page" ,
                    timer: 4000,
                    showConfirmButton: false
                });



                $(".submit").attr('disabled','disabled');
                $('input:checkbox').attr('disabled','disabled');

            }
        }

    });

});



function check_number(event) {
  var Consider = event.which || event.keyCode|| event.charCode;
  if (((Consider<48)||(Consider>57))&&(Consider!=8)){
      event.preventDefault();
  }


}

function phonenum_check(event) {
    var Consider = event.which || event.keyCode|| event.charCode;
    if (((Consider<48)||(Consider>57))&&(Consider!=8)){
        event.preventDefault();
    }


}

function  confirm(event) {
    var flag= [false,false,false,false,false,false];
    var name=$("#name").val();
    var fname=$("#familyname").val();
    if(name=="" || fname=="")
    {
        $("#namecontrol").text("this field can't be empty");
    }
    else
    {
        $("#namecontrol").text("");
        flag[0]=true;
    }

    var user=$("#username").val();
    if(user=="")
    {
        $("#usernamecontrol").text("username field can't be empty");
    }
    else
    {
        if (! /^[a-zA-Z0-9.]+$/.test(user)) {
            // Validation failed
            $("#usernamecontrol").text("username is necessary");
        }
        else
        {
            $("#usernamecontrol").text("");
            flag[1]=true;
        }
    }


    var pass=$("#password").val();
    if(pass=="")
    {
        $("#passcontrol").text(" password field is empty");
    }
    else
    {
        if(pass.length<8)
        {
            $("#passcontrol").text("password is shorter than 8 character");
        }
        else
        {
            $("#passcontrol").text("");
            flag[2]=true;
        }
    }



    var repass=$("#passcheck").val();
    if(repass=="")
    {
        $("#repasscontrol").text("password repeat field cant be empty");
    }
    else
    {
        if(repass!=pass)
        {
            $("#repasscontrol").text("password and repeat aren't same");
        }
        else
        {
            $("#repasscontrol").text("");
            flag[3]=true;
        }
    }



    var day= $("#day").val();
    var year=$("#year").val();
    if(day=="" || year=="")
    {
        $("#datecontrol").text("this field can't be empty");
    }
    else
    {
        if(day<1 || day>31)
        {
            $("#datecontrol").text("out of range");
        }
        else
        {
            $("#datecontrol").text("");
            flag[4]=true;
        }
    }


    var tel=$("#PhoneNumber").val();
    console.log(tel.indexOf("0"));
    if(tel=="")
    {
        $("#telcontrol").text("this field can't be empty");
    }
    else
    {
        if((tel.length!=13) || (tel.indexOf("+98")!=0) || (tel.lastIndexOf("+")!=0) )
        {
            $("#telcontrol").text("wrong format");
        }
        else
        {
            $("#telcontrol").text("");
            flag[5]=true;
        }

    }

    var j=0;
    var i=0;
    for(;i<6 && flag[i]==true;i++)
    {
        j=j+1;
    }

    if(j==6)
    {
        swal("Good job!", "enrolled successfully ", "success");
    }


}

function focus(id) {
    switch(id)
    {
        case 0 : $("#namecontrol").text("");break;
        case 1 : $("#usernamecontrol").text("");break;
        case 2 : $("#passcontrol").text("");break;
        case 3 : $("#repasscontrol").text("");break;
        case 4 : $("#datecontrol").text("");break;
        case 5 : $("#telcontrol").text("");break;
    }

}
