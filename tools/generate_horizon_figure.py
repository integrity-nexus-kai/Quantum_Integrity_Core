#!/usr/bin/env python3
"""Generate the current figure from the representative cubic, not an evolution model."""
from pathlib import Path
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def horizon(beta, outer):
    xc, bc = 2/3, (4/27)**(1/3)
    if beta == bc:
        return xc
    if beta == 0:
        return 1.0 if outer else np.nan  # x=0 is not a positive horizon
    lo, hi = (xc, 1.0) if outer else (0.0, xc)
    def p(x):
        return x**3-x**2+beta**3
    for _ in range(70):
        mid=(lo+hi)/2
        if (p(mid)>0) == outer:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def main():
    root=Path(__file__).resolve().parents[1]
    bc=(4/27)**(1/3)
    beta=np.linspace(0,bc,601)
    outer=np.array([horizon(float(b),True) for b in beta])
    inner=np.array([horizon(float(b),False) for b in beta])
    residual=max(float(np.nanmax(np.abs(x**3-x**2+beta**3))) for x in [outer,inner])
    assert residual < 2e-15
    assert np.all(np.diff(outer)<=1e-14) and np.all(np.diff(inner[1:])>=-1e-14)
    with plt.rc_context({'font.size':10,'axes.titlesize':12,'figure.dpi':150}):
        fig,ax=plt.subplots(figsize=(7.2,4.5),constrained_layout=True)
        ax.plot(beta,outer,color='#155c96',label='Outer horizon')
        ax.plot(beta,inner,color='#c26b18',ls='--',label='Inner horizon (beta > 0)')
        ax.axhline(1,color='#555555',ls=':',label='Schwarzschild horizon')
        ax.axvspan(bc,.62,color='#edf2f6')
        ax.axvline(bc,color='#777777',ls=':',lw=1)
        ax.scatter([bc],[2/3],color='#222222',s=28,zorder=5)
        ax.annotate('Critical double root\nx = 2/3',xy=(bc,2/3),xytext=(.32,.52),
                    arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=9)
        ax.text(.575,.28,'No positive\nhorizon',ha='center',fontsize=9)
        ax.set(xlim=(0,.62),ylim=(0,1.08),xlabel=r'$\beta=r_c/(2M)$',ylabel=r'$x=r_H/(2M)$',
               title='Horizons of the representative Hayward family')
        ax.grid(alpha=.2);ax.legend(loc='lower left',fontsize=8,framealpha=.95)
        path=root/'figures/tig_horizon_branches.png'
        fig.savefig(path,metadata={'Software':'QIC tools/generate_horizon_figure.py'})
        plt.close(fig)
    data={'source':'tools/generate_horizon_figure.py','equation':'x^3-x^2+beta^3=0',
          'domain':'M>0, beta>=0; inner horizon only beta>0', 'critical_beta':bc,'critical_x':2/3,
          'samples_per_branch':len(beta),'max_polynomial_residual':residual,
          'interpretation':'static representative geometry; no dynamical horizon formation',
          'image_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (root/'figures/tig_horizon_branches.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__ == '__main__':
    main()
