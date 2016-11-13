from gmpy2 import *

# Computing discrete log modulo prime.


def discrete_log(p, g, h, B):
    x1_table = {divm(h, powmod(g, i, p), p): i for i in range(B)}

    for x0 in range(B):
        x1_value = powmod(g, B*x0, p)
        x1 = x1_table.get(x1_value)

        if x1 is not None:
            return mpz(x0) * B + mpz(x1)


if __name__ == "__main__":
    p = mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
    g = mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
    h = mpz(3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333)
    B = mpz(2 ** 20)

    print(discrete_log(p, g, h, B))
