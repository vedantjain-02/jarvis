$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });

    // siri configuration
     var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style:"ios9",
    amplitude: "1",
    speed: "0.30",
    autostart:  true
    
  });

//   siri message animaton 

      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync:true,
        },
    });

    // mic button click event
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()

    });

    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
    
        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
             $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);  
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function playAssistant(message) {

        if (message != ""){

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false); 
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false); 
            $("#SendBtn").attr("hidden", true);

        }
    }  
    
    function showHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false); 
            $("#SendBtn").attr('hidden', true);   
        }
        else{
            $("#MicBtn").attr('hidden', true); 
            $("#SendBtn").attr('hidden', false); 
        }
    }

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        showHideButton(message)

    });

    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        playAssistant(message)

    });


    $("#chatbox").keypress(function (e) {
        key=e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            playAssistant(message)
        }
    });


});