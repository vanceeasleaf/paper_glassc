from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="glassC",
			method="greenkubo",
			nodes=2,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="shengbte"
		)
		app=dict(th=True,ekpoints=[2,2,2],engine='vasp',supercell=[2,2,2],kpoints=[5,5,5])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
