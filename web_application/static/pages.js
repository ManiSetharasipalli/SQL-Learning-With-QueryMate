function handleFormSubmission(formId,containerId){
    document.getElementById(formId).addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this);

    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const formContainer = document.getElementById(containerId);
        formContainer.innerHTML = `
            <div class="flex items-center justify-center p-4 ${data.result ? 'bg-green-200' : 'bg-red-100'} rounded-md shadow-md">
                <p class="text-lg font-semibold text-${data.result ? 'green' : 'red'}-800">
                    ${data.result ? 'Correct!' : 'Wrong!'}
                </p>
            </div>
        `;
    })
    .catch(error => console.error('Error:', error));
});
}
handleFormSubmission('Quiz','quiz-container')
handleFormSubmission('Exercise','exercise-container')


function buttons(button,text){
    document.getElementById(button).addEventListener('click',function(){
        document.getElementById(text).classList.toggle('hidden');
 });
}
buttons('hintButton','hintText')
buttons('ansButton','ansText')

function navigateTo(pageUrl, sidebarLinkSelector) {
    // Update the sidebar
    const parentWindow = window.parent;
    parentWindow.postMessage({ type: 'updateSidebar', selector: sidebarLinkSelector }, '*');
    // Navigate to the specified page
    window.location.href = pageUrl;
}
