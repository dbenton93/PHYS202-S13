def LinearLeastSquaresFit(x,y):
	n=float(len(x))
	xavg=(1/n)*(sum(x))
	yavg=(1/n)*(sum(y))
	xsqavg=(1/n)*(sum(x**2))
	xyavg=(1/n)*(sum(x*y))
	m=(xyavg-(xavg*yavg))/(xsqavg-(xavg)**2)
	b=((xsqavg*yavg)-(xavg*xyavg))/(xsqavg-(xavg)**2)
	denom=((n-2)*(xsqavg-(xavg)**2))
	merr=sqrt(((sum((y-(m*x+b))**2))/n)/denom)
	berr=sqrt(((sum((y-(m*x+b))**2))/n)*(xsqavg)/denom)
	return (m,b,merr,berr)

def WeightedLinearLeastSquaresFit(x,y,weight):
	w=sum(weight)
	weightless=True
	for i in weight:
		if i!=1:
			weightless=false
	if weightless:
		return LinearLeastSquaresFit(x,y)
	wx=sum(weight*x)
	wxsq=sum(weight*x**2)
	wy=sum(weight*y)
	wxy=sum(weight*x*y)
	b=(wxsq*wy-wx*wxy)/(w*wxsq-wx**2)
	m=(w*wxy-wx*wy)/(w*wxsq-wx**2)
	mer=(w/(w*wxsq-wx**2))**.5
	ber=(wxsq/(w*wxsq-wx**2))**.5
	return m,b,mer,ber

