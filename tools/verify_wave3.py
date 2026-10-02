#!/usr/bin/env python3
"""Exact and numerical checks for the bounded QIC wave-3 propagation model.

Requires SymPy (including mpmath). This is a same-run calculation verifier,
not a validation of TIG gravitational perturbations or an echo detection.
"""
import json
import sympy as sp
import mpmath as mp


def main():
    x, beta, d, eta, eps, y, r = sp.symbols('x beta d eta eps y r', real=True)
    M, ell, s, q = sp.symbols('M ell s q', positive=True)
    bc, xc, D0 = sp.root(4, 3)/3, sp.Rational(2, 3), sp.Rational(4, 9)
    P, D = x**3-x**2+beta**3, x**3+beta**3
    F = P/D
    checks = []

    def eq(name, lhs, rhs):
        assert sp.simplify(lhs-rhs) == 0, (name, lhs, rhs)
        checks.append(name)

    eq('critical denominator', D.subs({x:xc,beta:bc}), D0)
    eq('exact expansion above criticality', sp.expand(P.subs({x:xc+d,beta:bc+eta})),
       d**2+d**3+3*bc**2*eta+3*bc*eta**2+eta**3)
    eq('metric second derivative at criticality', sp.diff(F,x,2).subs({x:xc,beta:bc}), sp.Rational(9,2))
    eq('metric transverse derivative at criticality', sp.diff(F,beta).subs({x:xc,beta:bc}), 3*bc**2/D0)
    eq('positive-side scaled denominator', sp.limit(P.subs({x:xc+s*y,beta:bc+s**2/(3*bc**2)})/s**2,s,0), y**2+1)
    eq('negative-side scaled denominator', sp.limit(P.subs({x:xc+s*y,beta:bc-s**2/(3*bc**2)})/s**2,s,0), y**2-1)
    eq('arctangent primitive', sp.diff(sp.atan(d/s)/s,d), 1/(d**2+s**2))
    eq('logarithmic primitive', sp.diff(sp.log((d-s)/(d+s))/(2*s),d), 1/(d**2-s**2))
    eq('full bottleneck coefficient', 4*M*D0*sp.pi/(sp.sqrt(3)*bc), 16*sp.pi*M/(9*sp.sqrt(3)*bc))
    eq('half bottleneck coefficient', 4*M*D0*sp.pi/(2*sp.sqrt(3)*bc), 8*sp.pi*M/(9*sp.sqrt(3)*bc))
    eq('on-horizon derivative', (sp.diff(F,x).subs(beta**3,x**2-x**3)), 3-2/x)
    eq('surface gravity fold scaling', sp.limit((3-2/(xc+s))/(4*M*s),s,0), 1/(2*M*D0))
    eq('fixed-beta simple-horizon logarithmic coefficient', 2/((3-2/x)/(2*M)), 1/((3-2/x)/(4*M)))
    eq('exact critical factorization', F.subs(beta,bc), (x-xc)**2*(x+sp.Rational(1,3))/(x**3+sp.Rational(4,27)))
    eq('critical inverse-square coefficient', sp.limit(d**2/F.subs({x:xc+d,beta:bc}),d,0), D0)
    eq('Hayward metric identity', 1-2*M*r**2/(r**3+2*M*ell**2),
       (1-2*M*r**2/(r**3+sp.Symbol('rc')**3)).subs(sp.Symbol('rc')**3,2*M*ell**2))
    eq('Hayward critical beta cube', ell**2/(4*(3*sp.sqrt(3)*ell/4)**2), sp.Rational(4,27))
    # Derive the radial part of Box(Psi) rather than assume a wave potential.
    fr = sp.Function('F')(r)
    u = sp.Function('u')(r)
    radial = sp.expand(fr*sp.diff(r**2*fr*sp.diff(u/r,r),r)/r)
    eq('test-scalar radial wave operator', radial,
       fr**2*sp.diff(u,r,2)+fr*sp.diff(fr,r)*sp.diff(u,r)-fr*sp.diff(fr,r)*u/r)

    mp.mp.dps = 60
    bcm = (mp.mpf(4)/27)**(mp.mpf(1)/3)
    xcm, d0m = mp.mpf(2)/3, mp.mpf(4)/9
    Cplus = 4*d0m*mp.pi/(mp.sqrt(3)*bcm)
    Cmove = 2*d0m/(mp.sqrt(3)*bcm)*mp.log(3)  # q=2, M=1

    def inverse(z,b):
        return (z**3+b**3)/(z**3-z**2+b**3)

    values=[]
    for power in (2,3,4,6,8):
        h=mp.mpf(10)**(-power); width=mp.sqrt(3)*bcm*mp.sqrt(h)
        above=bcm+h
        tplus=4*mp.quad(lambda z:inverse(z,above),[mp.mpf('.4'),xcm-width,xcm,xcm+width,mp.mpf('1.5')])
        below=bcm-h
        root=mp.findroot(lambda z:z**3-z**2+below**3,(xcm+width*.8,xcm+width*1.2))
        mirror=root+width  # q=2 at leading order, strictly outside r_+
        pts=sorted(set([mirror]+[z for z in [xcm+3*width,xcm+30*width] if mirror<z<mp.mpf('1.5')]+[mp.mpf('1.5')]))
        tmove=4*mp.quad(lambda z:inverse(z,below),pts)
        tfixed=4*mp.quad(lambda z:inverse(z,below),[mp.mpf('.9'),mp.mpf('1.5')])
        values.append({'distance':str(h),'horizonless_full_crossing_ratio':float(tplus*mp.sqrt(h)/Cplus),
                       'tracking_exterior_mirror_ratio':float(tmove*mp.sqrt(h)/Cmove),
                       'fixed_exterior_delay_over_M':float(tfixed)})
    tcrit=4*mp.quad(lambda z:inverse(z,bcm),[mp.mpf('.9'),mp.mpf('1.5')])
    assert abs(values[-1]['horizonless_full_crossing_ratio']-1)<mp.mpf('.001')
    assert abs(values[-1]['tracking_exterior_mirror_ratio']-1)<mp.mpf('.005')
    assert abs(values[-1]['fixed_exterior_delay_over_M']/float(tcrit)-1)<mp.mpf('.00001')
    assert abs(values[-1]['horizonless_full_crossing_ratio']-1)<abs(values[0]['horizonless_full_crossing_ratio']-1)
    assert abs(values[-1]['tracking_exterior_mirror_ratio']-1)<abs(values[0]['tracking_exterior_mirror_ratio']-1)
    print(json.dumps({'verification':'PASS','assurance':'same-run / not independent',
       'sympy_version':sp.__version__,'mpmath_version':mp.__version__,
       'exact_checks':checks,'numerical_checks':5,'numerical_precision_decimal_digits':mp.mp.dps,
       'bottleneck_coefficient_over_M':float(Cplus),'tracking_coefficient_over_M_q2':float(Cmove),
       'fixed_exterior_critical_delay_over_M':float(tcrit),'numerical_samples':values,
       'boundary':'geometric round-trip delay with a prescribed reflector; no physical TIG echo or QM recovery proved'},indent=2))


if __name__ == '__main__':
    main()
