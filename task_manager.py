"""
Sistema de Gerenciamento de Tarefas
Este módulo implementa um sistema básico de gerenciamento de tarefas
com funcionalidades de adicionar, completar e listar tarefas.
"""

class Task:
    def __init__(self, title, description, priority="medium"):
        """
        Inicializa uma nova tarefa
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

class TaskManager:
    def __init__(self):
        """
        Inicializa o gerenciador de tarefas
        """
        self.tasks = []
    
    def add_task(self, title, description, priority="medium"):
        """
        Adiciona uma nova tarefa ao gerenciador
        """
        if not title or not description:
            raise ValueError("Título e descrição são obrigatórios")
        task = Task(title, description, priority)
        self.tasks.append(task)
        return len(self.tasks) - 1

    def complete_task(self, task_id):
        """
        Marca uma tarefa como concluída
        """
        if not (0 <= task_id < len(self.tasks)):
            raise IndexError("ID de tarefa inválido")
        self.tasks[task_id].completed = True
        return True

    def get_task_by_priority(self, priority):
        """
        Retorna todas as tarefas de uma determinada prioridade
        """
        return [task for task in self.tasks if task.priority == priority]

    def list_tasks(self):
        """
        Lista todas as tarefas no formato:
        [x] Task 1: Título (prioridade)
            Descrição da tarefa
        """
        if not self.tasks:
            print("Nenhuma tarefa encontrada!")
            return

        for i, task in enumerate(self.tasks):
            status = "✓" if task.completed else " "
            print(f"[{status}] Task {i}: {task.title} ({task.priority})")
            print(f"    {task.description}")
            print(f"    Criado em: {task.created_at.strftime('%d/%m/%Y %H:%M')}")

def main():
    """
    Função principal para demonstração do sistema
    """
    manager = TaskManager()
    
    # Adicionando tarefas de exemplo
    tasks = [
        ("Implementar Autenticação", "Criar sistema de login com JWT", "high"),
        ("Otimizar Banco de Dados", "Melhorar queries e adicionar índices", "medium"),
        ("Atualizar Documentação", "Documentar novas APIs REST", "low"),
        ("Testes Unitários", "Implementar testes para novos módulos", "high")
    ]

    for title, desc, priority in tasks:
        manager.add_task(title, desc, priority)

    print("\n=== Tasks Iniciais ===")
    manager.list_tasks()
    
    print("\n=== Completando primeira task ===")
    manager.complete_task(0)
    
    print("\n=== Tasks de Alta Prioridade ===")
    high_priority = manager.get_task_by_priority("high")
    for task in high_priority:
        print(f"- {task.title}")

    print("\n=== Lista Final ===")
    manager.list_tasks()

if __name__ == "__main__":
    from datetime import datetime
    main()