

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#phi for English language
phi_L = 0.0667
phi_0 = 1 / 26

# Ciphertext sent on mail
text = "TMWSXOSIKJHAZDCUODWFLWEYTPFIATHBUECJVIAWAWRFRHAVHLPZZHQFWEXEUHKGRNIVUSBZUEERSFXFVHYFETSJFSAVZFKSCEYIYCIESYSVPTSWTAXAVRFTPDJGMJOCDIKAPKISTGATHBUUETSKGFLQRDPLRGATPUZNIWWIJMWOJECMOKZIYGWSQPZPFETSFFXOSRMXOCIAXFCWZMZHFEFZHFFIHBUECZWJLIYAIKNVSXSVNSIQAOCDSVYWVVXOSSDEJYJEMAVRKMUSMWVZONECMOKZIYCIECTCKZIYOEVRLJVJWHKRFCSWBWRLGJGJLWKZIYCWLLLAWGVAVVAVKOPKALFVDSUUSWJVFVLLLRRQWVTGZSACXJEWVJECMWIKXMOEUMLGIWKHFUARNKYSXAVVQALFVDMRSNWVLIEJIHGFFEIZPVIYWMWHMFFEXOSZJXVASKXVBVKXOSJZEWSFXXOSCWXASIKSUAPXEAVVJWNOMWQLOEGHKWUWEAVRLLLKRKEZELSVLGKGYARRJOTOEOMAVTMVSMSDEJYYSMYTIGQAVVULHFRUXLFRFHAIIFSMHYWMUGTJMWHZGRHZJGKLCIYMHBROMMSFXXOSRTSCSZVVLKRULPZUAWOQFFGSIJASUHYSXTMDGXOSIOEZTIWGRZVVEURJAGRZPLSMWMWPPHKDIZHFFISCQWRNSJWEJVRTSBHRXSVHRFHHVRDJSCEYAOWTZALFVSVYOEYIKWESRLOKJSDPVKMKSKZIPFXJECSRFHDSIWWHQIWHACKZITSDGVFCWXMCSCAXAZVTVVHYWVZCWEMUSNZSNOMWYWHIQMUUKGKLHRDMCWEYIEQVWHPBXDCLOIDCPBKZEAIEAZLFJSPZHIMKNZVAETWEVIIHVVJVFRTISWVXMYSCAKPCLKPFSELIYHRARLRKZEAHYWCOOUSPSPVWRICIFSUHYWMYPRUOZKZLLAVVAVOOEVWPBKZIPFKJSBGVJWWCTCIAGRFHOOUFICSILERSELLLAFMXPBKZMZGKSXLCWWBPGKWRJSFMVZKRKXOSDSVZVTGYUHIQHVKETCAVVJMCSIOMAVZFEZHYWVPJVJAVIEVXDSELCTWCWWVTKZIZSRECMWIKXTCJLZPJZVEURSJSHRZETYSJKMVBFXXOSZVIUHZLCVTKZMUUJKILAJLSTSKGLHJVTILBXSMUSUGRHAVESYOSDIYONSJASIFSVBKGAHFUKICSEARNOKKYJVRLMTSZXSBBUGYATFJGLFKSMUHYSXAVZKFSSRCTSOTWSCSIYVVKEOMAVEWXAZVKAHGKZIJVLJGOMRJHHBULLHHGZMSWGHMYFZHPHHVGJAVZKTHFZKLHBUSPZCXWSYUZSRHKZXIVTKZIHPFNIDSIWHLOUSRKPLJMLRRFHAVRLESSOSRKSITEYHYGPVAVOEIFRZETHFTMHGRFHYCXWVPBWSRAQYAPKFVFSMHYWEMCIWWHWUOIYSRDWVRVSHHBUTYYWVVEURKZEAHYWHHFBXPHHNAPKSIFIZGSWCVBULLLQYMVJVPSVKWELIYGVUXLRNAXORPCIZOEVQVIEVWHBUYEASJOMAVJUEAHVJIKQRLXSSWWIKWEYSUWKOEZHYWQHFJZIZOEVXOOKLLLZFOPLOUWRSWEWFLMFFHDOJLLLFZNIYOEVXOOKLLLRZKXHBKKECOXWPHWIXVVANZMJVKZIDWEVAHGIMWOWEYAHGKZIZSRSRKHYSXAVVKQHZCTYURCWSMGYAZLFJYVVKZFKHTISMKCWAXHZCSRKPVYMUBZFKACTJCDOJHMWVFDHFCLJRVWJWGYWVVEASIJMIZVNSPQVSWHARFWAOILIKIGXVVARESUUKZINFRNIZOKLLLGZVIVTKZIJVLJGODFJGOYVWTZHZDPFCLDMAHCWHLJZDSYWCDGBHPGYYHYJSHHRXIHFWMPTOESPSWEUSHFJWKYSPOMAVRYVLOKAVVBFFLPGCWKHARFAPHYFSOOKSRKKZLL "


# Task 3 a) Using Friedman's method 2
# Friedman's method 2

""" 
Measure phi for the entire ciphertext
This is used to estimate the keylength m 
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
    m = (n*(phi_L-phi_0))/((n-1)* phi_T - (n*phi_0)+phi_L)
    # There is also a formula for when n is large
    print("Without rounding the m, we get: ", m)
    print("Rounding the m and our guess is", round(m))
    return round(m)


# b) ) Use Kasiski’s test or Friedman’s method 1 to determine the most likely length of the key
# that was used to encrypt your given ciphertext.

# Using Friedman's method 1, to finding the length of the key

def friedmans_method_1(m_estimate, text):
    tolerance = 0.01
    current_tolerance = 1
    m_closest = m_estimate

    i = 1
    count = 1
    up_or_down = -1 #This switches wheter we want to check one higher m or one lower
    while current_tolerance>tolerance: #This will run until we are close enough
        up_or_down*=-1
        m_current = m_closest+up_or_down*i
        print("This is m_current", m_current)
        if m_current<1:continue
        count +=1
        if count % 2 != 0:
            i+=1
        phi_values = []
        for j in range(m_current):
            text_shift= ""
            for k in range(j, len(text), m_current): #m_current is the step size
                text_shift+=text[k]
            # Adding all the phis computed to a list
            phi_values.append(phi_text(text_shift))

        phi_average = sum(phi_values)/len(phi_values)
        new_current_tolerance = abs(phi_average-phi_L)

        if new_current_tolerance <current_tolerance:
            current_tolerance=new_current_tolerance
            m_closest = m_current

    print("The cloest m w got: ", m_closest)
    return m_closest








def main():
    phi_t = phi_text(text)
    friedman2 = friedmans_method_2(phi_t, text)

    print("This is friedman2", friedman2)
    m_guess = friedman2
    friedman1 = friedmans_method_1(m_guess, text)
    print("This is friedman1", friedman1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
