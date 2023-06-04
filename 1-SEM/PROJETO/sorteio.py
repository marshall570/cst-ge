lista_nomes = ['Adriane dos Santos', 'Ana Letycia', 'Ana Lucia', 'Andre Oliveira', 'Augusto Belina', 'Camila Bonfim', 'Caroline Leal', 'Clarice Roseno', 'Ellen Suellen', 'Emanuelle Rodrigues', 'Fabiola Rodrigues', 'Felipe Moreno', 'Gabriel Moreno', 'Guilherme Pereira', 'Guilherme Vinicius', 'Gustavo Sergio', 'Iago Micaell', 'Jaiane Santos', 'Jaine Santana', 'Juliana Martins', 'Karoline Vitoria', 'Leticia Linguanote', 'Leticia Paula', 'Leticia Tupiniquim', 'Liana Ganiko', 'Lucas Azevedo', 'Lucileide de Assis', 'Mariana Nascimento', 'Miguel Moraes', 'Osvaldo Francisco', 'Paulo Jose', 'Phelipe Gabriel', 'Rafael Rufino', 'Renan Batista', 'Robson Joao', 'Selma Cristina', 'Soelia Vieira', 'Tatiana Ferreira', 'Thaina Fernanda', 'Thais Cristine', 'Thamires da Cunha', 'Thwanny Alcantara', 'Wellington Cimeno', 'Wynnie Alcantara']

counter = 0
groups = 1

print(f'GRUPO {groups}:')

for i in lista_nomes:
    if counter < 3:
        print(i)
        counter += 1
    
    else:
        groups +=1
        print(i + f'\n\n\nGRUPO {groups}:')
        counter = 0
