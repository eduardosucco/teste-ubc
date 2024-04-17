-- Create Alunos table
CREATE TABLE Alunos (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    MATRICULA VARCHAR(50),
    Nome VARCHAR(100),
    Idade INT,
    Genero VARCHAR(10),
    Bairro VARCHAR(100),
    Endereco VARCHAR(255),
    DataCriacao DATETIME
);

-- Create Materias table
CREATE TABLE Materias (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    Descricao VARCHAR(255),
    Professor VARCHAR(100),
    DataCriacao DATETIME
);

-- Create Notas table
CREATE TABLE Notas (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ALUNOID INT,
    MATERIAID INT,
    Nota DECIMAL(5, 2),
    SEMESTRE INT,
    DataCriacao DATETIME,
    FOREIGN KEY (ALUNOID) REFERENCES Alunos(ID),
    FOREIGN KEY (MATERIAID) REFERENCES Materias(ID)
);

-- Insert sample data into Alunos table
INSERT INTO Alunos (MATRICULA, Nome, Idade, Genero, Bairro, Endereco, DataCriacao) VALUES
('001', 'John Doe', 25, 'Male', 'Exampleville', '123 Main St', NOW()),
('002', 'Jane Doe', 22, 'Female', 'Sampletown', '456 Oak St', NOW()),
('003', 'Bob Smith', 24, 'Male', 'Testville', '789 Pine St', NOW()),
('004', 'Alice Johnson', 23, 'Female', 'Cityville', '987 Elm St', NOW()),
('005', 'Michael Brown', 26, 'Male', 'Townsville', '654 Maple St', NOW()),
('006', 'Sarah Johnson', 21, 'Female', 'Exampleville', '123 Main St', NOW()),
('007', 'David Smith', 24, 'Male', 'Sampletown', '456 Oak St', NOW()),
('008', 'Emily Davis', 23, 'Female', 'Testville', '789 Pine St', NOW()),
('009', 'Daniel Wilson', 22, 'Male', 'Cityville', '987 Elm St', NOW()),
('010', 'Olivia Brown', 25, 'Female', 'Townsville', '654 Maple St', NOW()),
('011', 'James Johnson', 26, 'Male', 'Exampleville', '123 Main St', NOW()),
('012', 'Sophia Smith', 21, 'Female', 'Sampletown', '456 Oak St', NOW()),
('013', 'Alexander Davis', 24, 'Male', 'Testville', '789 Pine St', NOW()),
('014', 'Isabella Wilson', 23, 'Female', 'Cityville', '987 Elm St', NOW()),
('015', 'Ethan Brown', 22, 'Male', 'Townsville', '654 Maple St', NOW()),
('016', 'Mia Johnson', 25, 'Female', 'Exampleville', '123 Main St', NOW()),
('017', 'Benjamin Smith', 21, 'Male', 'Sampletown', '456 Oak St', NOW()),
('018', 'Ava Davis', 24, 'Female', 'Testville', '789 Pine St', NOW()),
('019', 'William Wilson', 23, 'Male', 'Cityville', '987 Elm St', NOW()),
('020', 'Charlotte Brown', 22, 'Female', 'Townsville', '654 Maple St', NOW()),
('021', 'Daniel Johnson', 25, 'Male', 'Exampleville', '123 Main St', NOW()),
('022', 'Harper Smith', 21, 'Female', 'Sampletown', '456 Oak St', NOW()),
('023', 'Michael Davis', 24, 'Male', 'Testville', '789 Pine St', NOW()),
('024', 'Sophia Wilson', 23, 'Female', 'Cityville', '987 Elm St', NOW()),
('025', 'Elijah Brown', 22, 'Male', 'Townsville', '654 Maple St', NOW()),
('026', 'Amelia Johnson', 25, 'Female', 'Exampleville', '123 Main St', NOW()),
('027', 'James Smith', 21, 'Male', 'Sampletown', '456 Oak St', NOW()),
('028', 'Olivia Davis', 24, 'Female', 'Testville', '789 Pine St', NOW()),
('029', 'Benjamin Wilson', 23, 'Male', 'Cityville', '987 Elm St', NOW()),
('030', 'Emma Brown', 22, 'Female', 'Townsville', '654 Maple St', NOW()),
('031', 'Alexander Johnson', 25, 'Male', 'Exampleville', '123 Main St', NOW()),
('032', 'Ava Smith', 21, 'Female', 'Sampletown', '456 Oak St', NOW()),
('033', 'William Davis', 24, 'Male', 'Testville', '789 Pine St', NOW()),
('034', 'Charlotte Wilson', 23, 'Female', 'Cityville', '987 Elm St', NOW()),
('035', 'Daniel Brown', 22, 'Male', 'Townsville', '654 Maple St', NOW()),
('036', 'Mia Johnson', 25, 'Female', 'Exampleville', '123 Main St', NOW()),
('037', 'Benjamin Smith', 21, 'Male', 'Sampletown', '456 Oak St', NOW()),
('038', 'Ava Davis', 24, 'Female', 'Testville', '789 Pine St', NOW()),
('039', 'William Wilson', 23, 'Male', 'Cityville', '987 Elm St', NOW()),
('040', 'Charlotte Brown', 22, 'Female', 'Townsville', '654 Maple St', NOW()),
('041', 'Daniel Johnson', 25, 'Male', 'Exampleville', '123 Main St', NOW()),
('042', 'Harper Smith', 21, 'Female', 'Sampletown', '456 Oak St', NOW()),
('043', 'Michael Davis', 24, 'Male', 'Testville', '789 Pine St', NOW()),
('044', 'Sophia Wilson', 23, 'Female', 'Cityville', '987 Elm St', NOW()),
('045', 'Elijah Brown', 22, 'Male', 'Townsville', '654 Maple St', NOW()),
('046', 'Amelia Johnson', 25, 'Female', 'Exampleville', '123 Main St', NOW()),
('047', 'James Smith', 21, 'Male', 'Sampletown', '456 Oak St', NOW()),
('048', 'Olivia Davis', 24, 'Female', 'Testville', '789 Pine St', NOW()),
('049', 'Benjamin Wilson', 23, 'Male', 'Cityville', '987 Elm St', NOW()),
('050', 'Emma Brown', 22, 'Female', 'Townsville', '654 Maple St', NOW());

-- Insert sample data into Materias table
INSERT INTO Materias (Nome, Descricao, Professor, DataCriacao) VALUES
('Math', 'Introduction to Algebra', 'Prof. Johnson', NOW()),
('Physics', 'Mechanics Fundamentals', 'Prof. Smith', NOW()),
('Chemistry', 'Basic Concepts', 'Prof. Davis', NOW()),
('English', 'Grammar and Writing', 'Prof. Wilson', NOW()),
('History', 'World History', 'Prof. Brown', NOW());

-- Inserir dados de notas para os alunos em 5 matérias para os próximos 3 semestres
INSERT INTO Notas (ALUNOID, MATERIAID, Nota, DataCriacao, Semestre) 
SELECT 
    a.ID AS ALUNOID, 
    m.ID AS MATERIAID, 
    ROUND(RAND() * 10, 2) AS Nota, 
    NOW() AS DataCriacao,
    1 AS Semestre -- Semestre 1
FROM 
    Alunos a
    CROSS JOIN Materias m
WHERE 
    a.ID <= 50;

INSERT INTO Notas (ALUNOID, MATERIAID, Nota, DataCriacao, Semestre) 
SELECT 
    a.ID AS ALUNOID, 
    m.ID AS MATERIAID, 
    ROUND(RAND() * 10, 2) AS Nota, 
    NOW() AS DataCriacao,
    2 AS Semestre -- Semestre 2
FROM 
    Alunos a
    CROSS JOIN Materias m
WHERE 
    a.ID <= 50;

INSERT INTO Notas (ALUNOID, MATERIAID, Nota, DataCriacao, Semestre) 
SELECT 
    a.ID AS ALUNOID, 
    m.ID AS MATERIAID, 
    ROUND(RAND() * 10, 2) AS Nota, 
    NOW() AS DataCriacao,
    3 AS Semestre -- Semestre 3
FROM 
    Alunos a
    CROSS JOIN Materias m
WHERE 
    a.ID <= 50;
