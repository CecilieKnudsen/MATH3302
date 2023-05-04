# The English alphabet letters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# phi for English language
phi_L = 0.0667
phi_0 = 1 / 26

# Ciphertext sent on mail
text = "TMWSXOSIKJHAZDCUODWFLWEYTPFIATHBUECJVIAWAWRFRHAVHLPZZHQFWEXEUHKGRNIVUSBZUEERSFXFVHYFETSJFSAVZFKSCEYIYCIESYSVPTSWTAXAVRFTPDJGMJOCDIKAPKISTGATHBUUETSKGFLQRDPLRGATPUZNIWWIJMWOJECMOKZIYGWSQPZPFETSFFXOSRMXOCIAXFCWZMZHFEFZHFFIHBUECZWJLIYAIKNVSXSVNSIQAOCDSVYWVVXOSSDEJYJEMAVRKMUSMWVZONECMOKZIYCIECTCKZIYOEVRLJVJWHKRFCSWBWRLGJGJLWKZIYCWLLLAWGVAVVAVKOPKALFVDSUUSWJVFVLLLRRQWVTGZSACXJEWVJECMWIKXMOEUMLGIWKHFUARNKYSXAVVQALFVDMRSNWVLIEJIHGFFEIZPVIYWMWHMFFEXOSZJXVASKXVBVKXOSJZEWSFXXOSCWXASIKSUAPXEAVVJWNOMWQLOEGHKWUWEAVRLLLKRKEZELSVLGKGYARRJOTOEOMAVTMVSMSDEJYYSMYTIGQAVVULHFRUXLFRFHAIIFSMHYWMUGTJMWHZGRHZJGKLCIYMHBROMMSFXXOSRTSCSZVVLKRULPZUAWOQFFGSIJASUHYSXTMDGXOSIOEZTIWGRZVVEURJAGRZPLSMWMWPPHKDIZHFFISCQWRNSJWEJVRTSBHRXSVHRFHHVRDJSCEYAOWTZALFVSVYOEYIKWESRLOKJSDPVKMKSKZIPFXJECSRFHDSIWWHQIWHACKZITSDGVFCWXMCSCAXAZVTVVHYWVZCWEMUSNZSNOMWYWHIQMUUKGKLHRDMCWEYIEQVWHPBXDCLOIDCPBKZEAIEAZLFJSPZHIMKNZVAETWEVIIHVVJVFRTISWVXMYSCAKPCLKPFSELIYHRARLRKZEAHYWCOOUSPSPVWRICIFSUHYWMYPRUOZKZLLAVVAVOOEVWPBKZIPFKJSBGVJWWCTCIAGRFHOOUFICSILERSELLLAFMXPBKZMZGKSXLCWWBPGKWRJSFMVZKRKXOSDSVZVTGYUHIQHVKETCAVVJMCSIOMAVZFEZHYWVPJVJAVIEVXDSELCTWCWWVTKZIZSRECMWIKXTCJLZPJZVEURSJSHRZETYSJKMVBFXXOSZVIUHZLCVTKZMUUJKILAJLSTSKGLHJVTILBXSMUSUGRHAVESYOSDIYONSJASIFSVBKGAHFUKICSEARNOKKYJVRLMTSZXSBBUGYATFJGLFKSMUHYSXAVZKFSSRCTSOTWSCSIYVVKEOMAVEWXAZVKAHGKZIJVLJGOMRJHHBULLHHGZMSWGHMYFZHPHHVGJAVZKTHFZKLHBUSPZCXWSYUZSRHKZXIVTKZIHPFNIDSIWHLOUSRKPLJMLRRFHAVRLESSOSRKSITEYHYGPVAVOEIFRZETHFTMHGRFHYCXWVPBWSRAQYAPKFVFSMHYWEMCIWWHWUOIYSRDWVRVSHHBUTYYWVVEURKZEAHYWHHFBXPHHNAPKSIFIZGSWCVBULLLQYMVJVPSVKWELIYGVUXLRNAXORPCIZOEVQVIEVWHBUYEASJOMAVJUEAHVJIKQRLXSSWWIKWEYSUWKOEZHYWQHFJZIZOEVXOOKLLLZFOPLOUWRSWEWFLMFFHDOJLLLFZNIYOEVXOOKLLLRZKXHBKKECOXWPHWIXVVANZMJVKZIDWEVAHGIMWOWEYAHGKZIZSRSRKHYSXAVVKQHZCTYURCWSMGYAZLFJYVVKZFKHTISMKCWAXHZCSRKPVYMUBZFKACTJCDOJHMWVFDHFCLJRVWJWGYWVVEASIJMIZVNSPQVSWHARFWAOILIKIGXVVARESUUKZINFRNIZOKLLLGZVIVTKZIJVLJGODFJGOYVWTZHZDPFCLDMAHCWHLJZDSYWCDGBHPGYYHYJSHHRXIHFWMPTOESPSWEUSHFJWKYSPOMAVRYVLOKAVVBFFLPGCWKHARFAPHYFSOOKSRKKZLL"

# Task 3 a) Using Friedman's method 2
# Friedman's method 2

""" 
Measure phi for the entire ciphertext
This is used to estimate the key length m 
phi is the probability that two letters randomly selected
from a piece of text are equal
"""


def phi_text(ciphertext):
    n = len(ciphertext)
    sum_occurrences = 0
    for word in alphabet:
        n_i = ciphertext.count(word)
        sum_occurrences += n_i * (n_i - 1)

    phi_T = sum_occurrences / (n * (n - 1))

    return phi_T


def friedmans_method_2(phi_T, text):
    # Estimate m
    n = len(text)
    # Formula for computing m
    m = (n * (phi_L - phi_0)) / ((n - 1) * phi_T - (n * phi_0) + phi_L)
    # There is also a formula for when n is large
    print("Without rounding the m, we get: ", m)
    print("Rounding the m and our guess is", round(m))
    return round(m)


# b) Use Kasiski’s test or Friedman’s method 1 to determine the most likely length of the key
# that was used to encrypt your given ciphertext.

"""
Using Friedman's method 1, to finding the length of the key
that was used to encrypt the given ciphertext
"""


def friedmans_method_1(m_estimate, text):
    # Choosen tolerance for when we are getting close to phi for English
    tolerance = 0.01
    current_tolerance = 1
    m_closest = m_estimate

    i = 1
    # A counter knowing if we are incrementing or decrementing
    count = 1
    up_or_down = -1  # This switches wheter we want to check one higher m or one lower
    while current_tolerance > tolerance:  # This will run until we are close enough
        # Alternating between incrementing and decrementing
        up_or_down *= -1
        m_current = m_closest + up_or_down * i
        print("This is m_current", m_current)

        # No point in going below one
        if m_current < 1: continue
        count += 1

        # To make sure we go either up or down alternating times
        if count % 2 != 0:
            i += 1

        # Keeping track of the phi values
        phi_values = []

        for j in range(m_current):
            text_shift = ""
            for k in range(j, len(text), m_current):  # m_current is the step size
                text_shift += text[k]
            # Adding all the phis computed to a list
            phi_values.append(phi_text(text_shift))

        # Finding the average phi value
        phi_average = sum(phi_values) / len(phi_values)
        # Computing the tolerance, deciding if we are going to continue or not
        new_current_tolerance = abs(phi_average - phi_L)


        if new_current_tolerance < current_tolerance:
            # A better m is found
            current_tolerance = new_current_tolerance
            m_closest = m_current

    print("The cloest m w got: ", m_closest)
    return m_closest


# c) - Decrypt your given ciphertext and state the
#  keyword that was used to encrypt it

# Frequencies for letters in the English Alphabet
frequencies = {
    "A": 0.082, "N": 0.067,
    "B": 0.015, "O": 0.075,
    "C": 0.028, "P": 0.019,
    "D": 0.043, "Q": 0.001,
    "E": 0.127, "R": 0.060,
    "F": 0.022, "S": 0.063,
    "G": 0.020, "T": 0.091,
    "H": 0.061, "U": 0.028,
    "I": 0.070, "V": 0.010,
    "J": 0.002, "W": 0.023,
    "K": 0.008, "X": 0.001,
    "L": 0.040, "Y": 0.020,
    "M": 0.024, "Z": 0.001
}


def freq_analysis(text, m):
    # Sorting the dictionary based on value
    freq_sort = {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    # makes this into a list
    freq_sort = list(freq_sort)


    current_codeword = ""

    for i in range(m):
        text_shift = ""
        for j in range(i, len(text), m): # m is the stepsize
            text_shift += text[j]

        # Each shifted text then needs freq analysis
        text_frequencies = {}
        for a in alphabet:
            c = text_shift.count(a)
            text_frequencies[a] = c / len(text_shift) # normalize

        # List of most common words from the freq analysis of the text
        text_freq_sort = {k: v for k, v in sorted(text_frequencies.items(), key=lambda item: item[1], reverse=True)}
        text_freq_sort = list(text_freq_sort)


        distances = []
        for i in range(len(alphabet)):
            current_distance = alphabet.index(text_freq_sort[i]) - alphabet.index(freq_sort[i])
            current_distance %= 26
            distances.append(current_distance)

        shifted = max(set(distances), key=distances.count)
        alphabet_letter = alphabet[shifted]
        current_codeword += alphabet_letter
    print("Codeword found: ", current_codeword)
    # It is Horse
    return current_codeword


""" 
After finding the codeword we can decrypt 
"""


def decryption(text, codeword):
    # Method for decrypting the text
    result = ""
    n = len(text)
    m = len(codeword)
    for i in range(n):
        # To get the right index we do modulo
        code = i % m
        index = alphabet.index(text[i]) - alphabet.index(codeword[code])
        result += alphabet[(index) % 26]

    return result


def main():
    phi_t = phi_text(text)
    print("This is phi_t: ", phi_t)


    friedman2 = friedmans_method_2(phi_t, text)
    print("Answer 3a), this is friedman2: ", friedman2)

    m_guess = friedman2
    friedman1 = friedmans_method_1(m_guess, text)
    print("Answer 3b), this is friedman1: ", friedman1)

    codeword = freq_analysis(text, friedman1)
    print("Answer 3c), this is the codeword: ", codeword)

    result = decryption(text, codeword)
    print("Answer 3c), this is the result of the decryption: ", result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


