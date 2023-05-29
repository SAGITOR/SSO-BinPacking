public class Swarm {

	private final int ps = 25;
	private final int MaxIter = 10;

	private java.util.List<Salp> swarm = null;
	private Salp food = null;


	public void execute() {
		initRand();
		evolve();
	};

	private void initRand() {
		swarm = new java.util.ArrayList<>();
		food = new Salp();
		Salp s = null;
		for ( int i = 1; i <= ps; i++){
			do {
				s = new Salp();
			} while (!s.isFeasible());
			swarm.add(s);
		};

		food.copy(swarm.get(0));
		for ( int i = 0; i < ps; i++){
			if ( swarm.get(i).isBetterThan(food) ){
				food.copy(swarm.get(i));
			};
		};

		log(0);
	}

	private void evolve() {
		int t = 1;
		while (t <= MaxIter) {
			double c1 = 2.0*Math.pow(Math.E, -Math.pow( (4.0*t)/MaxIter ,2) );
			Salp s = new Salp();
			
			for ( int i = 0; i < ps; i++ ) {
				do {
					if(i == 0){
						s.copy(swarm.get(i));// suma 19
						s.leaderMove(food, c1);// suma 20
					}else{
						s.copy(swarm.get(i));
						s.followerMove(swarm.get(i - 1));
					};
					
				} while(!s.isFeasible());
				if ( s.isBetterThan(swarm.get(i)) ){// 19 > 20 ?
					swarm.get(i).copy(s); // 20 -> 19
				};
			};

			for ( int i = 0; i < ps; i++ ) {
				if ( swarm.get(i).isBetterThan(food) ){
					food.copy(swarm.get(i));
				};
			};

			log(t);
			t++;
		}
	}

	private void log(int t) {
		StdOut.printf("t=%d,\t%s\n", t, food);
	}
}