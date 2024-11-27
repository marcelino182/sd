const apiUrl = "http://127.0.0.1:5000/tasks"; // URL da API REST

const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");
const taskIdInput = document.getElementById("task-id");
const taskTitleInput = document.getElementById("task-title");
const taskDescriptionInput = document.getElementById("task-description");

// Carregar todas as tarefas
async function loadTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();
    taskList.innerHTML = ""; // Limpar a lista

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
}

// Criar ou atualizar uma tarefa
async function saveTask(event) {
    event.preventDefault();
    const taskId = taskIdInput.value;
    const taskData = {
        title: taskTitleInput.value,
        description: taskDescriptionInput.value,
    };

    const method = taskId ? "PUT" : "POST";
    const url = taskId ? `${apiUrl}/${taskId}` : apiUrl;

    const response = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(taskData),
    });

    if (response.ok) {
        taskForm.reset();
        loadTasks();
    } else {
        alert("Erro ao salvar a tarefa!");
    }
}

// Editar uma tarefa
async function editTask(taskId) {
    const response = await fetch(`${apiUrl}/${taskId}`);
    const task = await response.json();

    taskIdInput.value = task.id;
    taskTitleInput.value = task.title;
    taskDescriptionInput.value = task.description;
}

// Excluir uma tarefa
async function deleteTask(taskId) {
    const response = await fetch(`${apiUrl}/${taskId}`, { method: "DELETE" });
    if (response.ok) {
        loadTasks();
    } else {
        alert("Erro ao excluir a tarefa!");
    }
}

// Carregar tarefas no início
taskForm.addEventListener("submit", saveTask);
loadTasks();
