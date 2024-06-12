class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            closeButton: document.querySelector('.chatbox__close')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton, closeButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        closeButton.addEventListener('click', () => this.closeChatbox(chatBox)); // Added close button event listener

        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // Show or hide the box
        if (this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    closeChatbox(chatbox) {
        chatbox.classList.remove('chatbox--active'); // Hide the chatbox when the close button is clicked
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value.trim()
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "QueryMate", message: r.answer };
                this.messages.push(msg2);
                this.updateChatText(chatbox)
                textField.value = ''

            }).catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
                textField.value = ''
            });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function (item, index) {
            if (item.name === "QueryMate") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();

document.addEventListener('DOMContentLoaded', function () {

    var sidebarLinks = document.querySelectorAll('.sidebar a');
    // Add click event listener to each link
    sidebarLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            // Remove 'active' class from all links
            sidebarLinks.forEach(function (link) {
                link.classList.remove('active');
            });
            this.classList.add('active');
        });
    });


    // Get the search input
    var searchInput = document.getElementById('searchInput');
    // Add keyup event listener to the search input
    searchInput.addEventListener('keyup', function ({key}) {   // destructing assignment
        if (key === 'Enter') {
            // If Enter key is pressed, trigger the search and scroll to the result
            var searchResult = searchConcept();
            searchResult.classList.add('active');
            searchInput.value='';

        }
    });
});

function searchConcept() {
    var searchInput = document.getElementById('searchInput').value.toLowerCase();

    var sidebarLinks = document.querySelectorAll('.sidebar a');

    sidebarLinks.forEach(function (link) {
        link.classList.remove('active');
    });

    sidebarLinks.forEach(function (link) {
        var conceptName = link.innerText.toLowerCase();
        if (conceptName === searchInput) {
            // Show the result in the iframe
            var contentFrame = document.getElementsByName('content-frame')[0];
            contentFrame.src = link.href;

            // Scroll only within the SQL concepts container
            var sqlContainer = document.querySelector('.sidebar');
            sqlContainer.scrollTop = (link.offsetTop-sqlContainer.offsetTop) - 200;

            searchResult = link;
        }
    });
    return searchResult;
}

window.addEventListener('message', function(event) {
    if (event.data.type === 'updateSidebar') {
        // Remove the 'active' class from all links
        document.querySelectorAll('nav.sidebar ul li a').forEach(link => {
            link.classList.remove('active');
        });
        // Add the 'active' class to the specified link
        document.querySelector(`nav.sidebar ul li a[href="${event.data.selector}"]`).classList.add('active');
    }
});

