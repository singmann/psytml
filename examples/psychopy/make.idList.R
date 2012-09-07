
make.id.list <- function(n, objects, startValue = 1, append = FALSE, nshuffle = 0,  filename = "id.lst") {
	if (nshuffle %% length(objects) != 0) message("nshuffle adjusted to fit length(objects)")
	while(nshuffle %% length(objects) != 0) {
		nshuffle <- nshuffle+1
	}
	rep.s <- nshuffle/length(objects)
	
	nextra <- n-nshuffle
	
	if (nextra %% length(objects) != 0) message("nextra adjusted to fit length(objects)")
	while(nextra %% length(objects) != 0) {
		nextra <- nextra+1
	}
	rep.e <- nextra/length(objects)
	
	shuffled <- sample(rep(objects, rep.s), nshuffle)
	extra <- as.vector(vapply(1:rep.e, function(x) sample(objects, length(objects)), objects))
	
	conditions <- c(shuffled, extra)
	
	d.out <- data.frame(ns = (1:length(conditions)) + (startValue-1), conditions = conditions)
	
	write.table(d.out, file = filename, row.names = FALSE, col.names = FALSE, quote = FALSE, append = append)
}

make.id.list(60, c("causal", "noncausal"))
