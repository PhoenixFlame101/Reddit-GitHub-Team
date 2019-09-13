# I edited a bunch of code, removed redundant code etc.
# Haven't tested the code yet, so there might be some errors
# Haven't changed the algo; the program still does the same things

def encrypt(text, n):
    evens=[]
    odds=[]
    
    counter = 0
    
    if counter == n:
        return text
    else:
        for i in enumerate(text):
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        
            even_str = ''.join(evens)
            odd_str = ''.join(odds)
        
            answer = odd_str + even_str
            counter += 1

            if counter == n:
                return answer

def decrypt(encrypted_text, n):
        n_count = 0
        if n <= 0:
            return encrypted_text
        else:
            decrypted = ''
            for i in range(n):
                # Splitting the string that needs decrypting in half
                length = (len(encrypted_text))
                half_length = length//2
                       
                first_half = encrypted_text[:half_length]
                second_half = encrypted_text[half_length:]
                first_half = list(first_half)
                second_half = list(second_half)

                # Combining 1st of second_half, then 1st of first_half, etc into 1 string
                _decrypted = []
                
                for my_counter in range(half_length):
                    _decrypted.append(second_half[my_counter])
                    _decrypted.append(first_half[my_counter])
                    
                if length % 2 == 0:
                    pass
                else:
                    _decrypted.append(second_half[half_length])
                    
                _decrypted = ''.join(_decrypted)
                decrypted = _decrypted

            return decrypted

text = input()

decrypt(encrypt(text, 5))

input()