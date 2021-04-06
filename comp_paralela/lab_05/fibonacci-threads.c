#include <err.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*! \file  fibonacci-threads.c
 *  \brief Computes n-th Fibonacci number using POSIX threads.
 *
 *  $Id: fibonacci-threads.c,v 1.3 2010/05/30 21:17:11 nickf Exp $
 *
 */

/*! Thread routine takes n and computes F(n). */
static void* fibonacci_thread( void* arg )
{
	size_t n = ( size_t )arg, fib;
	int ern;
	pthread_t th1, th2;
	void* pvalue;

	switch ( n )
	{
		case 0:	 return ( void* )0;
		case 1:	 /* FALLTHRU */
		case 2:	 return ( void* )1;
		default: break;
	}

	if (( ern = pthread_create( &th1, 0, fibonacci_thread,
		( void* )( n - 1 )))) err( ern, "pthread_create" );

	if (( ern = pthread_create( &th2, 0, fibonacci_thread,
		( void* )( n - 2 )))) err( ern, "pthread_create" );

	if (( ern = pthread_join( th1, &pvalue )))
		err( ern, "pthread_join" );

	fib = ( size_t )pvalue;

	if (( ern = pthread_join( th2, &pvalue )))
		err( ern, "pthread_join" );

	fib += ( size_t )pvalue;

	return ( void* )fib;
}

/*! Computes \a n th Fibonacci number. */
size_t fibonacci( size_t n )
{
	return ( size_t )fibonacci_thread(( void* )n );
}

/* eof */

