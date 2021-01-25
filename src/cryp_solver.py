import os
import time

### FUNGSI UNTUK KONVERSI KATA MENJADI BILANGAN, INSPIRASI DARI: https://stackoverflow.com/questions/35975748/python3-cryptarithmetic-puzzle-generic-solution-in-python3
def word_val(word, letter_dict):
    total_val = 0
    factor = 1

    for letter in reversed(word):
        total_val += factor * letter_dict[letter]
        factor *= 10

    return total_val

### FUNGSI UNTUK MENGHASILKAN PERMUTASI DARI HIMPUNAN DIGIT, MODIFIKASI DARI: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
def permutation(digits_list, low_id, top_id): 
	if low_id == top_id: 
		yield digits_list
	else: 
		for i in range(low_id, top_id + 1):
			digits_list[low_id], digits_list[i] = digits_list[i], digits_list[low_id]

			yield from permutation(digits_list, low_id + 1, top_id)

			digits_list[low_id], digits_list[i] = digits_list[i], digits_list[low_id]

### FUNGSI UNTUK MENGECEK APAKAH ADA HURUF PERTAMA DARI SEBUAH KATA YANG MEMILIKI NILAI SUBSTITUSI = 0
def first_letter_not_zero(first_letter_list, substitution):
    val = True

    for letter in first_letter_list:
        if substitution[letter] == 0:
            val = False
            break
    
    return val

### FUNGSI UTAMA YANG SUDAH DIINTEGRASIKAN
def solve_cryptarithmetic(file_name):
    ### 1. AKSES FILE
    file_sample = open(file_name, 'r')
    Lines = file_sample.readlines() 

    ### 2. LISTING ALFABET PER BARIS DALAM FILE
    time_initialization = time.time()

    container = []              # --> LIST UNTUK HURUF
    container_text = []         # --> LIST UNTUK KATA MURNI
    set_first_letter = set()    # --> HIMPUNAN UNTUK HURUF PERTAMA TIAP KATA

    for line in Lines:
        container_text.append(''.join(c for c in line if c.isalnum()))
        text = list([val for val in line.strip() if val.isalpha()])
        container.append(text)
        if (len(text) > 0):
            set_first_letter.update(text[0])

    container_first_letter = list(set_first_letter)

    ### 3. MEMBUAT HIMPUNAN ALFABET DALAM FILE
    char_set = set()

    i = 0

    for i in range(len(container)):
        char_set.update(container[i])

    list_char_set = list(char_set)

    ### 4. MENAMPILKAN PROBLEM / SOAL
    print('PROBLEM:')

    i = 0
    for i in range(len(container_text)):
        if i < len(container_text) - 3:
            print(container_text[i] + ' + ', end = '')
        elif i == len(container_text) - 3:
            print(container_text[i] + ' = ', end = '')
        elif i == len(container_text) - 1:
            print(container_text[i])

    ### 5. MENAMPIILKAN SOLUSI
    print('\nSOLUTION: ')

    digits = list(range(10))        # --> LIST DIGIT
    digits_length = len(digits)

    total_test = 0

    time_first_calc = time.time()

    for permutation_val in permutation(digits, 0, digits_length - 1):
        sol = dict(zip(list_char_set, permutation_val))

        total_test += 1

        if first_letter_not_zero(container_first_letter, sol) == True:
            total_operand = 0
            j = 0
            container_substitution = []     # --> LIST KATA OPERAND YANG SUDAH DISUBSTITUSI

            for j in range(len(container_text) - 2):
                container_substitution.append(word_val(container_text[j], sol))
                total_operand += container_substitution[j]

            sum_value = word_val(container_text[-1], sol)       # --> HASIL JUMLAH YANG SUDAH DISUBSTITUSI

            if total_operand == sum_value:
                k = 0
                for k in range(len(container_substitution)):
                    if k != len(container_substitution) - 1:
                        print(str(container_substitution[k]) + ' + ', end = '')
                    else:
                        print(str(container_substitution[k]), end = '')
                print(' = ' + str(sum_value) + ' {} #TEST: {} #TIME: {:.5f}'.format(sol, total_test, time.time() - time_first_calc))

    time_fin = time.time()

    ### 6. MENAMPILKAN INFORMASI TAMBAHAN
    print('\nNUMBER OF TEST: ' + str(total_test))
    print('FIRST CALCULATION: {:.5f}'.format(time_first_calc - time_initialization))
    print('TOTAL TIME FOR CALCULATION: {:.5f}'.format(time_fin - time_first_calc))
    print('TOTAL PROGRAM TIME: {:.5f}'.format(time_fin - time_initialization))

if __name__ == '__main__':
    current_dirr = os.path.dirname(__file__)
    parent_dirr = os.path.split(current_dirr)[0]
    file_path = os.path.join(parent_dirr, 'test')
    
    for file_name in os.scandir(file_path):
        solve_cryptarithmetic(file_name)
        print()