
public class Salp extends Problem{
    private int[] x = new int[nVars];

    public Salp (){
		for ( int j = 0; j < nVars; j++ ) {
			x[j] = StdRandom.uniform(2);
		};
    };

    protected void leaderMove( Salp food, double c1 ){
        for ( int j = 0; j < nVars; j++ ){
            double c2 = Math.random();//necesario, definido en el Swarm no mejora el fitness 
            double c3 = Math.random() - 0.5;
            x[j] = toBinary( c3 >= 0 ? food.x[j] + c1*c2 : food.x[j] - c1*c2 );
        };
    };
    
    protected void followerMove( Salp previousFollower ){
        for ( int j = 0; j < nVars; j++ ){
            x[j] = toBinary( (0.5)* (x[j] + previousFollower.x[j]) );
            //x[j] = toBinary( Math.random() * (x[j] + previousFollower.x[j]) + Math.random() );
        };

    };

    protected boolean isFeasible() {
        return checkConstraint(x);
    };

    protected int computeFitness() {
		return computeFitness(x);
	};

    protected boolean isBetterThan (Salp g){
        return computeFitness() < g.computeFitness();
    };

    protected void copy(Object object){
        if ( object instanceof Salp ){
			System.arraycopy(((Salp) object).x, 0, this.x, 0, nVars);
        };
    };

	private String showSolution() {
		return java.util.Arrays.toString(x);
	}

	private float diff() {
		return computeFitness(x) - optimum();
	}

	private float rpd() {
		return diff() / optimum() * 100f;
	}

    private int toBinary(double x) {
		return StdRandom.uniform(0.5, 0.731059) <= (1 / (1 + Math.pow(Math.E, -x))) ? 1 : 0;
	};

    @Override
	public String toString() {
        return String.format("optimal value: %d, fitness: %d, diff: %.1f, rpd: %.2f%%, p: %s\n", optimum(),
            computeFitness(), diff(), rpd(), showSolution());
	}
    
};