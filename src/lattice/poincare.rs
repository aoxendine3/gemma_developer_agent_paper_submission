//! 18,432-Dimensional Poincaré Hyperbolic Manifold & Möbius Gyrovector Addition Engine

pub const POINCARE_NORM_BOUND: f64 = 0.85;

/// Compute Euclidean norm of vector slice
pub fn norm(v: &[f64]) -> f64 {
    v.iter().map(|x| x * x).sum::<f64>().sqrt()
}

/// Poincaré Contraction Projection Gate (\pi_{\le 0.85})
pub fn poincare_projection(v: &mut [f64]) {
    let current_norm = norm(v);
    if current_norm > POINCARE_NORM_BOUND {
        let scale = POINCARE_NORM_BOUND / current_norm;
        for x in v.iter_mut() {
            *x *= scale;
        }
    }
}

/// Conformal factor \lambda_x at point x
pub fn conformal_factor(x: &[f64]) -> f64 {
    let n = norm(x);
    let n_sq = (n * n).min(0.999999);
    2.0 / (1.0 - n_sq)
}

/// Möbius Gyrovector Addition: u \oplus_{\mathbb{B}} v
pub fn mobius_addition(u: &[f64], v: &[f64], out: &mut [f64]) {
    assert_eq!(u.len(), v.len());
    assert_eq!(u.len(), out.len());

    let norm_u_sq = u.iter().map(|x| x * x).sum::<f64>();
    let norm_v_sq = v.iter().map(|x| x * x).sum::<f64>();
    let dot_uv = u.iter().zip(v.iter()).map(|(a, b)| a * b).sum::<f64>();

    let num_u = 1.0 + 2.0 * dot_uv + norm_v_sq;
    let num_v = 1.0 - norm_u_sq;
    let denom = (1.0 + 2.0 * dot_uv + norm_u_sq * norm_v_sq).max(1e-12);

    for i in 0..u.len() {
        out[i] = (num_u * u[i] + num_v * v[i]) / denom;
    }

    poincare_projection(out);
}
