const apiUrl = "http://127.0.0.1:5000";
let token = "";

// Referências aos elementos
const loginForm = document.getElementById("login-form");
const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");

// Função para mostrar/ocultar formulários
function toggleLogin(show) {
    if (show) {
        loginForm.classList.add("active");
        taskForm.style.display = "none";
        taskList.style.display = "none";
    } else {
        loginForm.classList.remove("active");
        taskForm.style.display = "block";
        taskList.style.display = "block";
    }
}

// Função de login
async function login(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    const response = await fetch(`${apiUrl}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
        const data = await response.json();
        token = data.access_token;
        toggleLogin(false);
        loadTasks();
    } else {
        alert("Login inválido!");
    }
}

// Função para carregar tarefas
async function loadTasks() {
    const response = await fetch(`${apiUrl}/tasks`, {
        headers: { Authorization: `Bearer ${token}` },
    });

    if (response.ok) {
        const tasks = await response.json();
        taskList.innerHTML = "";
        Object.values(tasks).forEach(task => {
            const li = document.createElement("li");
            li.innerHTML = `
                <span>
                    <strong>${task.title}</strong> - ${task.description}
                </span>
                <div class="actions">
                    <button onclick="editTask(${task.id})">Editar</button>
                    <button onclick="deleteTask(${task.id})">Excluir</button>
                </div>
            `;
            taskList.appendChild(li);
        });
    } else {
        alert("Erro ao carregar tarefas!");
    }
}

// Função para salvar tarefa
async function saveTask(event) {
    event.preventDefault();
    const taskId = document.getElementById("task-id").value;
    const taskData = {
        title: document.getElementById("task-title").value,
        description: document.getElementById("task-description").value,
    };

    const method = taskId ? "PUT" : "POST";
    const url = taskId ? `${apiUrl}/tasks/${taskId}` : `${apiUrl}/tasks`;

    const response = await fetch(url, {
        method,
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(taskData),
    });

    if (response.ok) {
        taskForm.reset();
        loadTasks();
    } else {
        alert("Erro ao salvar a tarefa!");
    }
}

// Função para deletar tarefa
async function deleteTask(taskId) {
    const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
    });

    if (response.ok) {
        loadTasks();
    } else {
        alert("Erro ao excluir a tarefa!");
    }
}

// Eventos
document.getElementById("form-login").addEventListener("submit", login);
taskForm.addEventListener("submit", saveTask);

// Mostrar o formulário de login inicialmente
toggleLogin(true);
