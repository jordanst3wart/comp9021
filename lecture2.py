# a single program from the second lecture
# this code can be used like: "from lecture2.py import function_name"
# use -v verbose to check extra info

def get_inputs():
    print('We want to compute a fraction...')
    sigma = input('Please input sigma: ')
    tau = input('Please input tau: ')
    print(*simplify_fraction(*compute_fraction(sigma, tau)))


def compute_fraction(sigma, tau):
    numerator = sigma*(10**len(tau)-1)+int(tau)
    denominator = (10**len(tau)-1)*10**len(sigma)
    return numerator, denominator


def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p % q)


def simplify_fraction(p,q):
    gcd_of_pq = gcd(p,q)
    return p // gcd_of_pq, q // gcd_of_pq

# get input off user
def get(value):
    # do something here


get_inputs()


#
#
