eel.expose(updateAssistant);


function updateAssistant(answer) {
    let text = document.getElementById('assistant-ans');
    text.innerHTML = answer
}