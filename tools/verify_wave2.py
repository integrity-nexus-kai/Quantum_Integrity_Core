#!/usr/bin/env python3
"""Exact checks for QIC-01/02/03; requires SymPy, prints JSON evidence."""
import json
import sympy as s


def verify():
    checks = []

    def equal(name, actual, expected=0):
        residual = s.simplify(actual - expected)
        if residual != 0:
            raise AssertionError((name, residual))
        checks.append(name)

    t, r, theta, phi = s.symbols('t r theta phi', real=True)
    M, a = s.symbols('M a', positive=True)
    mu, cosmological, alpha, curvature = s.symbols('mu Lambda alpha R', real=True)
    F = s.Function('F')(r)
    coordinates = (t, r, theta, phi)
    metric = s.diag(-F, 1/F, r**2, r**2*s.sin(theta)**2)
    inverse = metric.inv()
    gamma = [[[s.simplify(sum(inverse[i,k] * (
        s.diff(metric[k,j], coordinates[l]) + s.diff(metric[k,l], coordinates[j])
        - s.diff(metric[j,l], coordinates[k])) for k in range(4))/2)
        for l in range(4)] for j in range(4)] for i in range(4)]
    ricci = s.zeros(4)
    for i in range(4):
        for j in range(4):
            ricci[i,j] = s.simplify(sum(
                s.diff(gamma[k][i][j], coordinates[k])
                - s.diff(gamma[k][i][k], coordinates[j])
                + sum(gamma[k][i][j]*gamma[l][k][l]
                      - gamma[l][i][k]*gamma[k][j][l] for l in range(4))
                for k in range(4)))
    scalar = s.simplify(s.trace(inverse * ricci))
    equal('Ricci scalar from Christoffel symbols', scalar,
          -s.diff(F,r,2) - 4*s.diff(F,r)/r + 2*(1-F)/r**2)
    equal('mixed Ricci t/r equality', (inverse*ricci)[0,0]-(inverse*ricci)[1,1])
    u = s.Function('u')(r)
    hessian = s.Matrix(4, 4, lambda i,j:
        s.diff(u,coordinates[i],coordinates[j])
        - sum(gamma[k][i][j]*s.diff(u,coordinates[k]) for k in range(4)))
    box = s.simplify(s.trace(inverse*hessian))
    equal('radial scalar dAlembertian', box, s.diff(r**2*F*s.diff(u,r),r)/r**2)
    equal('mixed f(R) t/r residual difference',
          -2*mu*((inverse*hessian)[0,0]-(inverse*hessian)[1,1]),
          2*mu*F*s.diff(u,r,2))

    lapse = 1 - 2*M*r**2/(r**3+a)
    R = s.factor(scalar.subs(F,lapse).doit())
    equal('representative Ricci scalar', R, 12*M*a*(2*a-r**3)/(r**3+a)**3)
    box_R = s.factor(s.diff(r**2*lapse*s.diff(R,r),r)/r**2)
    trace = s.factor(6*mu*box_R - R + 4*cosmological)
    equal('vacuum trace core limit', s.limit(trace,r,0,dir='+'), 4*cosmological-24*M/a)
    equal('vacuum trace infinity limit', s.limit(trace,r,s.oo), 4*cosmological)
    equal('asymptotically flat vacuum obstruction',
          s.limit(r**6*trace.subs(cosmological,0),r,s.oo), 12*M*a)
    equal('Schwarzschild limiting curvature', s.simplify(R.subs(a,0)))
    equal('Schwarzschild full vacuum Ricci',
          sum(v**2 for v in ricci.subs(F,1-2*M/r).doit()))
    equal('action coefficient convention',
          (curvature-2*cosmological)/(16*s.pi)+alpha*curvature**2,
          (curvature-2*cosmological+16*s.pi*alpha*curvature**2)/(16*s.pi))
    f = curvature-2*cosmological+mu*curvature**2
    equal('quadratic trace cancellation', curvature*s.diff(f,curvature)-2*f,
          -curvature+4*cosmological)
    equal('scalaron mass about constant curvature',
          (s.diff(f,curvature)-curvature*s.diff(f,curvature,2))/(3*s.diff(f,curvature,2)),
          1/(6*mu))

    x, beta, delta, epsilon = s.symbols('x beta delta epsilon', real=True)
    P = x**3-x**2+beta**3
    equal('horizon numerator',
          s.cancel(lapse.subs(r,2*M*x).subs(a,(2*M*beta)**3)),
          P/(x**3+beta**3))
    equal('discriminant', s.discriminant(P,x), beta**3*(4-27*beta**3))
    xc = s.Rational(2,3)
    bc = (s.Rational(4,27))**s.Rational(1,3)
    equal('critical polynomial', P.subs({x:xc,beta:bc}))
    equal('critical derivative', s.diff(P,x).subs(x,xc))
    equal('fold second derivative', s.diff(P,x,2).subs(x,xc), 2)
    equal('fold transverse derivative', s.diff(P,beta).subs(beta,bc), 3*bc**2)
    equal('critical factorization', P.subs(beta,bc), (x-xc)**2*(x+s.Rational(1,3)))
    equal('exact local fold expansion',
          s.expand(P.subs({x:xc+delta,beta:bc-epsilon})),
          delta**2+delta**3-3*bc**2*epsilon+3*bc*epsilon**2-epsilon**3)
    # A quadratic already has a fold and the Schwarzschild-normalized x=1 root.
    Q = x**2-x+beta
    equal('quadratic fold counterexample', Q.subs({x:s.Rational(1,2),beta:s.Rational(1,4)}))
    equal('quadratic fold derivative', s.diff(Q,x).subs(x,s.Rational(1,2)))
    assert s.diff(Q,x,2) != 0 and s.diff(Q,beta) != 0
    checks.append('quadratic fold nondegeneracy')
    # Two different smooth mass profiles share both asymptotic requirements.
    rc = s.symbols('rc', positive=True)
    alternative = M*r**3/(r**2+rc**2)**s.Rational(3,2)
    equal('alternative mass Schwarzschild limit', s.limit(alternative,r,s.oo), M)
    equal('alternative mass regular-core limit', s.limit(alternative/r**3,r,0), M/rc**3)
    assert s.simplify(alternative-M*r**3/(r**3+rc**3)) != 0
    checks.append('regularity and Schwarzschild limit do not uniquely select the mass profile')
    return {'verification': 'PASS', 'assurance': 'same-run, not independent',
            'sympy_version': s.__version__, 'checks': checks,
            'assumptions': ['metric formalism', 'signature -+++', 'G=c=1',
                            'M>0', 'a=rc^3>0', 'r>0', 'constant finite mu and Lambda'],
            'ricci_scalar': str(R), 'box_R': str(box_R),
            'vacuum_trace': str(trace),
            'vacuum_obstruction': {'Lambda_required_at_infinity': '0',
                                   'r6_trace_limit_with_Lambda0': str(12*M*a),
                                   'core_trace_limit_with_Lambda0': str(-24*M/a)},
            'conclusion': 'This nontrivial representative metric is not a vacuum solution of constant-coefficient quadratic metric f(R). A specified matter source has not been demonstrated.',
            'critical_x': str(xc), 'critical_beta': str(bc),
            'horizon_exponent': '1/2, local nondegenerate fold for the specified mass profile',
            'echo_exponent': 'NOT_CHECKED_WAVE2'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
